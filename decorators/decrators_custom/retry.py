# -*- coding: utf-8 -*-
import time
from functools import wraps


def retry(func):
    """UI case 重试3次机制"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                print("尝试第{}次执行：{}".format(i + 1, func.__name__))
                result = func(*args, **kwargs)
                print("尝试第{}次执行成功：{}".format(i + 1, func.__name__))
                return result
            except Exception as e:
                print("尝试第{}次执行失败{}失败，重试中：{}".format(i + 1, func.__name__, e))
                time.sleep(0.5)
        raise Exception("3次执行全部失败{}".format(func.__name__))

    return wrapper


if __name__ == "__main__":
    pass
