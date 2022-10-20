# -*- coding: utf-8 -*-
from functools import wraps


def swapper(func):
    print("init temp")

    @wraps(func)
    def temp(*arg, **kwargs):
        print(temp.__name__)

    return temp


if __name__ == "__main__":
    pass
