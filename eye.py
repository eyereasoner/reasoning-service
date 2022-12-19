import os
import subprocess
import time
from typing import Tuple

from helpers import generate_uuid, log
from config import KEEP_TEMP_FILES


class Eye:
    def __init__(self) -> None:
        self.data = []
        self.queries = []
        self.options = [
            "--no-qnames",  # No prefixes, easier to partition triples later
            "--quiet",  # No comments (timing, eye version and argments)
            "--nope",  # No proof explanation
            "--pass",  # Full deductive closure without filter/query
        ]
        self.temp_files = []
        self.temp_dir = "/tmp/"

    def add_queries(self, *queries) -> None:
        # pass outputs the full deductive closure, has to be removed when
        # filtering with queries
        if "--pass" in self.options:
            self.options.remove("--pass")
        self.queries.extend(*queries)

    def add_data_by_reference(self, *data) -> None:
        self.data.extend(*data)

    def add_data_by_value(self, data) -> None:
        temp_file_name = (
            f"{self.temp_dir}" f'{time.strftime("%Y%m%d-%H%M%S")}-{generate_uuid()}.ttl'
        )
        temp_file = open(temp_file_name, "w")
        temp_file.write(data)
        temp_file.close()
        self.temp_files.append(temp_file_name)
        log(f"Created temp file {temp_file_name}")

    def cleanup(self) -> None:
        if not KEEP_TEMP_FILES:
            for file in self.temp_files:
                log(f"Deleting {file}")
                os.remove(file)
        else:
            log("Keeping temp files")
            for file in self.temp_files:
                log(f"{file}")

    def serialize_command(self) -> str:
        return (
            ["swipl", "-x", "/usr/local/lib/eye.pvm", "--"]
            + self.data
            + self.temp_files
            + [v for file in self.queries for v in ("--query", file)]
            + self.options
        )

    def reason(self) -> Tuple[str, int]:
        try:
            process = subprocess.run(
                self.serialize_command(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding="utf-8",
                check=True,
            )
            log(process.stderr)
            return process.stdout, process.returncode
        except subprocess.CalledProcessError as cpe:
            log(cpe.stderr)
            return cpe.stderr, cpe.returncode
        finally:
            self.cleanup()
