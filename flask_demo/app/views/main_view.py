# -*- coding: utf-8 -*-
from . import main_bp


@main_bp.route("/", methods=["GET"])
def index():
    return "hello world"
