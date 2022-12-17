# -*- coding: utf-8 -*-
import time
from functools import wraps


def timer(func):
    """函数计时器"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        print("{}函数执行耗时 {:.2f}s".format(func.__name__, t1 - t0))
        return result

    return wrapper
