# -*- coding: utf-8 -*-
from . import main_bp


@main.route("/", methods=["GET"])
def index():
    return "hello world"
