import os
from pathlib import Path

from flask import Response, make_response, request
from helpers import error, log

from eye import Eye

CONFIG_DIR = os.getenv("CONFIG_DIR") or "/config/"


@app.route("/reason/", defaults={"path": None}, methods=["GET", "POST"])
@app.route("/reason/<path:path>", methods=["GET", "POST"])
def reason_with_config(path) -> Response:
    log(f"{request.method} {path}")
    if "data" not in request.values:
        msg = f"No data in to reason upon {path}"
        log(f"400 {msg}")
        return error(msg, status=400)
    eye = Eye()

    if path is not None:
        config = Path(f"{CONFIG_DIR}/{path}")
        if config.exists():
            queries = [query.resolve() for query in config.glob("*.n3q")]
            if queries:
                eye.add_queries(queries)
            eye.add_data_by_reference([data.resolve() for data in config.glob("*.n3")])
        else:
            msg = f"No config for {path}"
            log(f"404 {msg}")
            return error(msg, status=404)

    data_content = request.values["data"]
    assert isinstance(data_content, str)
    if data_content.startswith("http"):
        eye.add_data_by_reference(data_content.split(","))
    else:
        eye.add_data_by_value(data_content)

    data, code = eye.reason()

    if code:
        log(f"500 {path}")
        return error(data, status=500)
    else:
        response = make_response(data)
        response.mimetype = "text/turtle"
        log(f"200 {path}")
        return response
