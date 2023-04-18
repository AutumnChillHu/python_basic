# -*- coding: utf-8 -*-
from flask import Flask

from flask_demo.app.views import main_bp, task_bp, database_bp
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(database_bp)

    return app


def create_db(app):
    db = SQLAlchemy(app)
    return db
