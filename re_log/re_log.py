import logging
from logging.handlers import RotatingFileHandler

_logger = None


def _log_re():
    global _logger
    if _logger:
        return _logger
    logger = logging.getLogger('uvicorn.access')
    logger.setLevel(level=logging.DEBUG)
    handler = RotatingFileHandler(filename='log/monica.log', mode='a', encoding='UTF-8')
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)

    if logger.handlers:
        logger.handlers.clear()

    logger.handlers = [handler, console]

    _logger = logger
    return _logger


def log(*args):
    for it in args:
        _log_re().debug(it)
