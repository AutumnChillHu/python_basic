# # -*- coding: utf-8 -*-
#
# 校验测试学生使用装饰器实现适用于多个case的前置步骤，代码复用。
#
# def test_student_check(func):
#     @wraps(func)
#     def wrapped_function(student_id=None, *args, **kwargs):
#         # 校验学生是否是测试学生
#         if not kwargs.get('studentId'):
#             return '未获取到学生ID'
#         if not check_student_type(kwargs.get('studentId')):
#             return '学生不是测试学生，不允许进行操作'
#         return func(student_id, *args, **kwargs)
#
#     return wrapped_function
#
#
# UI
# case重试机制
#
#
# def retry(func):
#     '''重试3次装饰器
#     '''
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         for i in range(3):
#             try:
#                 logger.info("尝试第{}次执行：{}".format(i + 1, func.__name__))
#                 result = func(*args, **kwargs)
#                 logger.info("尝试第{}次执行成功：{}".format(i + 1, func.__name__))
#                 return result
#             except Exception as e:
#                 logger.info("尝试第{}次执行失败{}失败，重试中：{}".format(i + 1, func.__name__, e))
#                 time.sleep(0.5)
#         raise Exception("尝试3次全部执行失败{}".format(func.__name__))
#
#     return wrapper
#
#
# python
# built - in装饰器 @ property：将一个方法的调用方式变成属性调用 @ property：相当于get方法。
#
# @property.setter
#
# ：相当于set方法。如果没有定义这个方法，是不允许修改属性的。
#
# class Employee:
#     @property
#     def salary(self):
#         return 30000
#
#     @salary.setter
#     def salary(self, increment):
#         return 30000 + increment
#
#
# if __name__ == "__main__":
#     em = Employee()
#     print(em.salary, type(em.salary))
#     em.salary = 10000
#     print(em.salary, type(em.salary))
# // 输出
# 30000 <
#
#
# class 'int'>
#
#
# 20000 <
#
#
# class 'int'>
#
#
# 其他：打印日志、计时器（如下）
#
# import time
# from functools import wraps
#
#
# def timer(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         print("{}() finished in {} seconds".format(func.__name__, round(time.time() - start_time, 3)))
#         return result
#
#     return wrapper
#
#
# @timer
# def show():
#     print("a function in class")
#     time.sleep(3)
#
# // 调用
# show()
# // 输出
# a
# function in
#
#
# class
#     show()
#     finished in 3.002
#     seconds