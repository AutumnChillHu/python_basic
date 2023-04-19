# -*- coding: utf-8 -*-
from flask import Blueprint

main_bp = Blueprint("main", __name__)  # url_prefix默认为空
task_bp = Blueprint("task", __name__, url_prefix="/task")

from . import main_view, task_view
