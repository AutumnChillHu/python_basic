# -*- coding: utf-8 -*-
from flask_demo.manage import db


class TaskInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    state = db.Column(db.Integer, nullable=False)
