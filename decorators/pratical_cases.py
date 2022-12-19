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


def if_test_student(func):
    """测试用例前置条件，提炼重复步骤，代码复用：校验是否是测试学生。"""

    @wraps(func)
    def wrapper(student_id=None, *args, **kwargs):
        if not kwargs.get('studentId'):
            return "未获取到学生ID"
        if not get_student_type(kwargs.get('studentId')):
            return "学生不是测试学生，不允许进行操作"
        return func(student_id, *args, **kwargs)

    return wrapper


def get_student_type(student_id):
    pass
