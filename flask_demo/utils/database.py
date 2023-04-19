# -*- coding: utf-8 -*-
import threading

from flask_demo.config.paths import DB_ENV_PATH
from flask_demo.utils.load import load_ini
import pymysql


class DB(object):
    _pool = None

    @staticmethod
    def init():
        db = DB()
        return db

    def __init__(self, env=None):
        db_info = load_ini(DB_ENV_PATH)[env] if env else load_ini(DB_ENV_PATH)["test"]
        # 数据库初始化
        self.host = db_info["host"]
        self.port = int(db_info["port"])
        self.user = db_info["user"]
        self.pwd = db_info["pwd"]
        self.database = db_info["database"]
        self.conn = None
        self.active = False

    def _start(self):
        if not self.active:
            self.connect()

    def connect(self):
        # 连接数据库
        try:
            connection = pymysql.connect(
                host=self.host,
                port=int(self.port),
                user=self.user,
                password=self.pwd,
                database=self.database,
                # cursorclass=pymysql.cursors.DictCursor,
                charset="utf8",
                use_unicode=True)
            print("{0} :database is connecting successful".format(self.host))
            self.conn = connection
        except Exception as e:
            print("{0} :database is connecting failed : {1}".format(self.host, e))

    def query_one(self, sql):
        # 查询一个
        self._start()
        cursors = self.conn.cursor()
        print("execute query one sql: {0}".format(sql))

        try:
            lock = threading.Lock()
            lock.acquire()
            cursors.execute(sql)
            result = cursors.fetchone()
            lock.release()
            return result

        except Exception as e:
            print("query one is error sql = {0} msg = {1}".format(sql, e))
            return None

    def query_all(self, sql):
        # 查询所有
        self._start()
        cursors = self.conn.cursor()
        print("execute query all sql: {0}".format(sql))
        try:
            lock = threading.Lock()
            lock.acquire()
            cursors.execute(sql)
            result = cursors.fetchall()
            lock.release()
            # log.info("query all result: {0}".format(result))
            return result
        except Exception as e:
            print("query all is error sql = {0} msg = {1}".format(sql, e))
            return None

    def change_datas(self, sql, args=None):
        # 增，删，改
        self._start()
        cursors = self.conn.cursor()
        print("inert into sql: {0}".format(sql))
        try:
            lock = threading.Lock()
            lock.acquire()
            result = cursors.execute(sql, args)
            cursors.close()
            self.conn.commit()
            lock.release()
            print("inert into reault sql = {0} msg = {1}".format(sql, result))
            return result
        except Exception as e:
            print("inert into error sql = {0} msg = {1}".format(sql, e))
            return None

    def batch_insert(self, sql, values):
        try:
            self._start()
            cursors = self.conn.cursor()
            result = cursors.executemany(sql, values)
            cursors.close()
            self.conn.commit()
            return result
        except Exception as err:
            print("import failed with error: {0}".format(err))
            return None

    def closes(self):
        # 关闭数据库连接
        self._start()
        try:
            self.active = False
            self.conn.close()
            print("database is closed: {0}".format(self.host))
        except Exception as e:
            self.active = False
            print("database is closed error: {0}".format(e))
            raise "server is error {0}".format(e)
