# -*- coding: utf-8 -*-
"""
1.写不写return? —— no_return()、all_return()
"""

def no_return():
    """函数中完全没有return语句"""
    pass

def all_return(value):
    """
    函数中所有分支都有return语句
    要么return一个值，要么return None
    """
    if value:
        return value
    return None


if __name__ == "__main__":
    pass
