# -*- coding: utf-8 -*-
from functools import wraps


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


if __name__ == "__main__":
    pass
