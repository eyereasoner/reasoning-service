import subprocess
import os
from pathlib import Path
from helpers import *


class Eye:

    def __init__(self) -> None:
        self.data = []
        self.queries = []
        self.options = ['--nope', '--pass']
        self.temp_files = []
        self.temp_dir = 'temp/'

    def add_queries(self, *queries):
        if '--pass' in self.options:
            self.options.remove('--pass')
        self.queries.extend(*queries)
        pass

    def add_data_by_refernce(self, *data):
        self.queries.extend(*data)
        pass

    def data_by_value(data):
        pass

    def cleanup(self):
        for file in self.temp_files:
            os.remove(file)

    def serialize_command(self) -> str:
        cmd = ['eye']
        return (
            cmd +
            self.data +
            [v for file in self.queries for v in ('--query', file)] +
            self.options
        )

    def reason(self, *args, **kwargs):
        popen = subprocess.Popen(
            self.serialize_command(),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        for stdout_line in iter(popen.stdout.readline, ""):
            yield stdout_line
        popen.stdout.close()
        self.cleanup()
        return_code = popen.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, 'eye')
