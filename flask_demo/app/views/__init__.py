# -*- coding: utf-8 -*-
from flask import Blueprint

main = Blueprint("main", __name__)  # url_prefix默认为空
task = Blueprint("task", __name__, url_prefix="/task")
database = Blueprint("database", __name__, url_prefix="/database")

from . import main_view, database_view, task_view
