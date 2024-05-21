import json
from datetime import datetime
from pathlib import Path
from typing import Optional

from re_log import log


def get_absolute_path(file: str) -> Optional[Path]:
    return Path(file).resolve()


def write_to_json(file_name: str, data: dict) -> Optional[Path]:
    file_path = Path(f'json/{file_name}.json')
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    log(f'save json: {file_path}')
    return file_path


def named(prefix=None) -> str:
    timestamp = int(datetime.now().timestamp())
    if prefix is not None:
        return f'{prefix}_{timestamp}'
    return str(timestamp)


def load_json(file: Optional[Path]):
    with open(file, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    log(f'load json: {file}')
    return data
