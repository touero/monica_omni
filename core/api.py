from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any
from starlette.responses import JSONResponse
from pathlib import Path

from re_log import log
from util.util import write_to_json, named, load_json

app = FastAPI()


@app.get("/monica/preview/{item}")
async def preview(item: str):
    file = Path('json') / item
    log(f'GET /monica/preview/{item}: {file}')
    if file.exists():
        return load_json(file)
    else:
        raise HTTPException(status_code=404, detail=f"Path {item} does not exist")


class AnyData(BaseModel):
    describe_word: str
    data: Any


@app.post("/monica/any/")
async def accept_any(any_data: AnyData):
    log(f'POST /monica/any/: {any_data.dict()}')
    file_path = write_to_json(named(any_data.describe_word), any_data.dict())
    return JSONResponse(content={"result": f"http://127.0.0.1:2518/monica/preview/{file_path.name}"}, status_code=200)


