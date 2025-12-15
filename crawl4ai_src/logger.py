import os
import sys
import logging
import contextlib

## Create the logger writer and redirection for standard output

class LoggerWriter:
    def __init__(self, level=logging.INFO):
        self.logger = logging.getLogger("crawl4ai")
        self.level = level

    def write(self, msg: str) -> None:
        if msg.strip():
            self.logger.log(self.level, msg.rstrip())

    def flush(self) -> None:
        pass

log_path = os.path.join(os.getcwd(), "crawl4ai.log")
logger = logging.getLogger("crawl4ai")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

@contextlib.contextmanager
def redirect_stdout_to_logger(level=logging.INFO):
    original_stdout = sys.stdout
    sys.stdout = LoggerWriter(level)
    try:
        yield
    finally:
        sys.stdout = original_stdout
