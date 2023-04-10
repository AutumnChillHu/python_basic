# -*- coding: utf-8 -*-
from flask import Blueprint

main = Blueprint("main", __name__)  # url_prefix默认为空
login = Blueprint("login", __name__, url_prefix="/login")
mycenter = Blueprint("mycenter", __name__, url_prefix="/mycenter")
task = Blueprint("task", __name__, url_prefix="/task")

from . import main_view, login_view, mycenter_view, task_view
