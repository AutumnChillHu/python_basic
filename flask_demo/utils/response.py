# -*- coding: utf-8 -*-
from enum import Enum


class HttpStatusCode(Enum):
    """状态码枚举"""

    OK = (0, "成功")
    ERROR = (-1, "错误")
    ARGS_ERROR = (400, "参数错误")


def response_dict(status_code=None, code=None, msg=None, data=None, **kwargs):
    response = {"data": data}
    response["code"] = status_code.name if status_code else code
    response["msg"] = status_code.value if status_code else msg
    for key, value in kwargs.items():
        response[key] = value

    return response
