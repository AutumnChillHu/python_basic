# -*- coding: utf-8 -*-
"""
    1.写不写return? —— no_return()、all_return()
    2.函数内部涉及对参数的原地修改，return OR return var? —— update_return()
"""


def no_return():
    """函数中完全没有return语句
    但是个人认为，最好是return True/False 0/1 None，最好是给一个输出。
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
    调用函数时可能：
    1.update_return(arr):     arr会被影响，此时return None 和 return arr效果一样。
    2.update_return(arr[:]):  arr不会被影响，如果只是return None，那么经过原地修改的arr就无法得到了。

    所以如果对入参有原地/不原地修改的，建议都要返回具体值。
    """
    if len(arr) > 1:
        arr[0], arr[1] = arr[1], arr[0]
    return arr


if __name__ == "__main__":
    pass
