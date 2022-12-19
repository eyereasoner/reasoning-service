import os

CONFIG_DIR = os.getenv("CONFIG_DIR") or "/config/"

KEEP_TEMP_FILES = False
if isinstance(os.getenv('MODE'), str):
    KEEP_TEMP_FILES = os.getenv("MODE").lower() == 'development'
