# -*- coding: utf-8 -*-
from flask import Flask

from flask_demo.app.views import login, mycenter, task, main


def create_app():
    app = Flask(__name__)
    # print(__name__)

    app.register_blueprint(main)
    app.register_blueprint(login)
    app.register_blueprint(mycenter)
    app.register_blueprint(task)

    return app
