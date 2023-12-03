# -*- coding: utf-8 -*-
from configparser import ConfigParser

import yaml


def load_yml(filepath):
    file = open(filepath, mode='r', encoding='utf-8')
    return yaml.safe_load(file)


def load_ini(filepath):
    config = ConfigParser()
    config.read(filepath, encoding='utf-8')
    dict = {}
    for section in config.sections():
        dict[section] = {}
        for options in config.options(section):
            dict[section][options] = config.get(section, options)
    return dict


def load_sql(sqlfile, sqlname, *arg, **kwargs):
    sqlfile = load_yml(sqlfile)
    try:
        if sqlname in sqlfile:
            sql = sqlfile[sqlname].replace('\n', '')
            return sql.format(*arg, **kwargs)
    except Exception as e:
        raise 'replace sql is error:{0}'.format(e)
