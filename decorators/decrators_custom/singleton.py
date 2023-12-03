# -*- coding: utf-8 -*-
"""单例模式"""
from functools import wraps


def singleton(cls): #传递cls参数，因为装饰器是修饰类的，而非函数。
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


if __name__ == "__main__":
    pass
