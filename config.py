import os
from helpers import log

CONFIG_DIR = os.getenv("CONFIG_DIR") or "/config/"

KEEP_TEMP_FILES = os.getenv("KEEP_TEMP_FILES") or False
if not KEEP_TEMP_FILES and isinstance(os.getenv("MODE"), str):
    KEEP_TEMP_FILES = os.getenv("MODE").lower() == "development"


TIMEOUT = os.getenv("TIMEOUT") or 1200  # 20 minutes

log("Configuration: ")
log(f"  KEEP_TEMP_FILES: {KEEP_TEMP_FILES}")
log(f"  TIMEOUT: {TIMEOUT}s")
