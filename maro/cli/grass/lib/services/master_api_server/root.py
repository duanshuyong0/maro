# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.


import time

from flask import Flask

from .blueprints.containers import blueprint as containers_blueprint
from .blueprints.image_files import blueprint as image_files_blueprint
from .blueprints.jobs import blueprint as jobs_blueprint
from .blueprints.master import blueprint as master_blueprint
from .blueprints.nodes import blueprint as nodes_blueprint
from .blueprints.schedules import blueprint as schedules_blueprint

# App related

app = Flask(__name__)
app.url_map.strict_slashes = False

# Blueprints related

app.register_blueprint(blueprint=containers_blueprint)
app.register_blueprint(blueprint=image_files_blueprint)
app.register_blueprint(blueprint=jobs_blueprint)
app.register_blueprint(blueprint=master_blueprint)
app.register_blueprint(blueprint=nodes_blueprint)
app.register_blueprint(blueprint=schedules_blueprint)


@app.route("/status", methods=["GET"])
def status():
    return {
        "status": "OK",
        "time": time.time()
    }