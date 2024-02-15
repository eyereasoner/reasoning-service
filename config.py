import os
from helpers import log

CONFIG_DIR = os.getenv("CONFIG_DIR") or "/config/"

KEEP_TEMP_FILES = os.getenv("KEEP_TEMP_FILES") or False
if not KEEP_TEMP_FILES and isinstance(os.getenv("MODE"), str):
    KEEP_TEMP_FILES = os.getenv("MODE").lower() == "development"


TIMEOUT = int(os.getenv("TIMEOUT")) or 1200  # 20 minutes

STACK_LIMIT = os.getenv("STACK_LIMIT") or "8g"

log("Configuration: ")
log(f"  KEEP_TEMP_FILES: {KEEP_TEMP_FILES}")
log(f"  TIMEOUT: {TIMEOUT}s")
log(f"  STACK_LIMIT: {STACK_LIMIT}")
