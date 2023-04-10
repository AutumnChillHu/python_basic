# -*- coding: utf-8 -*-
from flask import Blueprint

login = Blueprint("login", __name__) #url_prefix默认为
mycenter = Blueprint("mycenter", __name__, url_prefix="mycenter")
task = Blueprint("task", __name__, url_prefix="task")
