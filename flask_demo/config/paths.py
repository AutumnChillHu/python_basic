# -*- coding: utf-8 -*-
import os

# paths.py所在目录config
CONFIG_PTAH = os.path.split(os.path.realpath(__file__))[0]
# dbenv.ini
DB_ENV_PATH = os.path.join(CONFIG_PTAH, 'dbenv.ini')
# task_info.yml路径
SQL_TASK_PATH = os.path.join(CONFIG_PTAH, 'sql/task.yml')
