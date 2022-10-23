# -*- coding: utf-8 -*-
from functools import wraps


def dontknow(func):
    print("init temp",func.__name__)

    @wraps(func)
    def wrapper(*arg, **kwargs):
        print("ss")

    return wrapper


if __name__ == "__main__":
    pass
