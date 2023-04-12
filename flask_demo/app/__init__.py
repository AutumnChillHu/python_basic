# -*- coding: utf-8 -*-
from flask import Flask

from flask_demo.app.views import main, task, database


def create_app():
    app = Flask(__name__)

    app.register_blueprint(main)
    app.register_blueprint(task)
    app.register_blueprint(database)

    return app
