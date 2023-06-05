# -*- coding: utf-8 -*-
import pymysql


class MySqlBaseOPeration(object):
    def __init__(self):
        self.conn = None

    def connect(self):
        pass
