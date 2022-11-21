from flask import request, stream_with_context, Response
import os
from pathlib import Path
from lib.eye import Eye

default_options = {
  'data': [],
  'data_uris': [],
  'query': 'pass'
}

CONFIG_DIR = '/app/config/'


@app.route("/hello")
def hello():
    return "Hello from the mu-python-template!"


# @app.route("/", methods=['GET', 'POST'])
def reason():
    data = []
    if 'data' not in request.values:
        return 'No data in to reason upon', 400
    else:
        # data can be urls or ttl
        data_content = request.values['data']
        assert isinstance(data_content, str)
        if data_content.startswith('http'):
            data = data_content.split(',')
        else:
            pass  # TODO
    eye = Eye()
    return Response(stream_with_context(eye.reason()))


@app.route("/", defaults={'path': None},methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def reason_with_config(path):
    if 'data' not in request.values:
        return 'No data in to reason upon', 400
    eye = Eye()
    if path is None:
        return 'default'
    else:
        config = Path(f'{CONFIG_DIR}/{path}')
        if config.exists():
            eye.add_queries([query.resolve() for query in config.glob('*.n3q')])
            eye.add_data_by_refernce([data.resolve() for data in config.glob('*.n3')])
        else:
            return 'Not found', 404

    data_content = request.values['data']
    assert isinstance(data_content, str)
    if data_content.startswith('http'):
        eye.add_data_by_refernce(data_content.split(','))
    else:
        pass  # TODO
    return Response(stream_with_context(eye.reason()))

