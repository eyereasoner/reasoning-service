from flask import request, make_response
from pathlib import Path
from eye import Eye
from helpers import error, log

CONFIG_DIR = '/config/'

@app.route("/reason/", defaults={'path': None}, methods=['GET', 'POST'])
@app.route('/reason/<path:path>', methods=['GET', 'POST'])
def reason_with_config(path):
    log(f'{request.method} {path}')
    if 'data' not in request.values:
        msg = f'No data in to reason upon {path}'
        log(f'400 {msg}')
        return error(msg, status=400)
    eye = Eye()

    if path is not None:
        config = Path(f'{CONFIG_DIR}/{path}')
        if config.exists():
            eye.add_queries([query.resolve() for query in config.glob('*.n3q')])
            eye.add_data_by_reference([data.resolve() for data in config.glob('*.n3')])
        else:
            msg = f'No config for {path}'
            log(f'404 {msg}')
            return error(msg, status=404)

    data_content = request.values['data']
    assert isinstance(data_content, str)
    if data_content.startswith('http'):
        eye.add_data_by_reference(data_content.split(','))
    else:
        eye.add_data_by_value(data_content)

    data, code = eye.reason()
    http_code = 200 if not code else 400
    log(f'{http_code} {path}')
    return make_response(data, http_code)
