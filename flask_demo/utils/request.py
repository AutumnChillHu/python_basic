# -*- coding: utf-8 -*-
"""Flask.request 请求对象"""
from flask import request
import json


def flask_request_attrs():
    """Flask.request 请求对象的常用属性"""
    # todo 了解下json格式！！！！
    get_data = {}

    get_data["header"] = request.headers
    get_data["cookie"] = request.cookies # 字典格式

    get_data["param_get"] = request.args  # ImmutableMultiDict格式，获取到GET参数
    get_data["param_post_str"] = request.get_data()  # 字符串格式，获取POST参数
    get_data["param_json"] = request.get_json()  # json格式，获取POST参数
    get_data["param_str"] = request.data  # 字符串形式 GET?
    get_data["param_"] = request.values

    get_data["file"] = request.files  # MultiDict格式，获取上传的文件

    print(get_data)


def get_request_params():
    if request.method == 'GET':
        # 访问MultiDict/ImmutableMultiDict，如果key不存在，会返回HTTP 400
        # 推荐转化成Dict，如果key不存在，会报KeyError
        data = request.args.to_dict()
    else:
        data = json.loads(request.get_data(), encoding='utf8')
    return data


if __name__ == "__main__":
    d = {1: 1, 2: 2}
    print(d[1])
    print(d.get(3))
