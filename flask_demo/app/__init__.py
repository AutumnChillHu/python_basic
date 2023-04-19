# -*- coding: utf-8 -*-
from flask import Flask

from flask_demo.app.views import main_bp, task_bp
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_bp)
    app.register_blueprint(task_bp)

    return app


def create_db_models(app):
    db = SQLAlchemy(app)
    # 只有第一次执行的时候会建库建表，之后需要先drop_all()再create_all()才能起效。
    db.create_all()
    return db
