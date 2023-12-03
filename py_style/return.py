# -*- coding: utf-8 -*-
"""
    1.写不写return?  no_return() 或者 all_return()
    2.函数内部涉及对参数的原地修改，return OR return var? —— update_return()
"""


def no_return():
    """函数中完全没有return语句，就不用写。
    显示获取没有return语句的函数返回值时，为None。
    """
    pass


def all_return(value):
    """
    1.如果有return语句，所有分支都要有return语句
    2.要么return一个值，要么明确返回None。不建议单独写个return。
    """
    if value:
        return value
    return None


def update_return(arr):
    """
    调用函数时，传参可能：直接引用(旧瓶装旧酒)/分片(新瓶装旧酒)/深复制(新瓶装新酒)
    通过调用函数时的穿参方式来控制。
    """
    pass


if __name__ == "__main__":
    pass
