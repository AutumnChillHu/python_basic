# -*- coding: utf-8 -*-
from flask import Blueprint

main_bp = Blueprint("main", __name__)  # url_prefix默认为空
task_bp = Blueprint("task", __name__, url_prefix="/task")
database_bp = Blueprint("database", __name__, url_prefix="/database")

from . import main_view, database_view, task_view
