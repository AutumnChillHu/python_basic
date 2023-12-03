# -*- coding: utf-8 -*-
import os

# config目录
from utils.load import load_ini

CONFIG_PTAH = os.path.split(os.path.realpath(__file__))[0]
# db_config.ini路径
DB_ENV_PATH = os.path.join(CONFIG_PTAH, "db_config.ini")
# sql.yml路径
SQL_PATH = os.path.join(CONFIG_PTAH, "sql.yml")

# 测试环境数据库连接URI
db_config = load_ini(DB_ENV_PATH)
DB_URI_TEST = "mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8" % (db_config["test"]["user"], db_config["test"]["pwd"],
                                                               db_config["test"]["host"], db_config["test"]["port"],
                                                               db_config["test"]["database"])
