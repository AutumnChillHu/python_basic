# -*- coding: utf-8 -*-
"""
1.写不写return? —— no_return()、all_return()
2.对参数进行原地修改的，return OR return X? —— inplace_return()
"""


def no_return():
    """函数中完全没有return语句"""
    pass


def all_return(value):
    """
    函数中所有分支都有return语句
    要么return一个值，要么明确返回None
    """
    if value:
        return value
    return None


def inplace_return(arr):
    """
    调用函数时可能：
    1.inplace_return(arr):      arr会被影响，此时 return 和 return arr效果一样。
    2.inplace_return(arr[:]):   arr不会被影响，如果只是 return，那么经过原地修改的arr就无法得到了。
    所以如果对入参有原地/不原地修改的，一定要返回具体值。
    """
    if len(arr) > 1:
        arr[0], arr[1] = arr[1], arr[0]
    return arr


if __name__ == "__main__":
    pass
