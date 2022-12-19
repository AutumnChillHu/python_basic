# -*- coding: utf-8 -*-
'''
基于函数、类实现（带参数）装饰器
'''

from functools import wraps


def without_params(func):
    """基于函数实现不带参数的装饰器"""
    # 传递函数层
    print("@{}装饰器的外部函数只为{}()函数启动一次".format(without_params.__name__, func.__name__))

    @wraps(func)
    def wrapper(*args, **kwargs):
        # 装饰器具体实现层
        print("@{}装饰器的内部函数被{}()函数调用".format(without_params.__name__, func.__name__))
        return func(*args, **kwargs)

    print("@{}装饰器的外部函数只为{}()函数启动一次完毕".format(without_params.__name__, func.__name__))

    return wrapper


def without_params_noreturn(func):
    """基于函数实现不带参数的装饰器"""
    # 传递函数层
    print("@{}装饰器的外部函数只为{}()函数启动一次".format(without_params.__name__, func.__name__))

    @wraps(func)
    def wrapper(*args, **kwargs):
        # 装饰器具体实现层
        result = func(*args, **kwargs)  # 直接执行了
        print("@{}装饰器的内部函数被{}()函数调用".format(without_params.__name__, func.__name__))
        return result

    print("@{}装饰器的外部函数只为{}()函数启动一次完毕".format(without_params.__name__, func.__name__))

    return wrapper


def with_params(li, text="hello"):
    """基于函数实现带参数的装饰器"""
    # 传递参数层
    print("@{}装饰器的 最外部函数 启动一次".format(with_params.__name__))

    def pass_func(func):
        # 传递函数层
        print("@{}装饰器的 传递函数层函数 只为{}()函数启动一次".format(with_params.__name__, func.__name__))

        @wraps(func)
        def wrapper(*args, **kwargs):
            """装饰器具体实现层"""
            print("@{}装饰器的 内部函数 被{}()函数调用".format(with_params.__name__, func.__name__))
            print('args:{}, kwargs:{}'.format(args, kwargs))
            print('params:{}, {}'.format(text, li))
            return func(*args, **kwargs)

        print("@{}装饰器的 传递函数层函数 只为{}()函数启动一次完毕".format(with_params.__name__, func.__name__))
        return wrapper

    print("@{}装饰器的最外部函数启动一次完毕".format(with_params.__name__))
    return pass_func


# @with_params([1, 2, 3])
# def func1(name):
#     name += "MO"
#     return None
#
#
# @with_params(li=[1, 2, 3])
# def func2(name):
#     name += "MO"
#     return None
#
#
# @with_params(li=[1, 2, 3], text="hello world", )
# def func3(name):
#     name += "MO"
#     return None
#
#
# func1("hxj")
# func2("hxj")
# func3("hxj")


class WithoutParams():
    """基于类实现的不带参数的装饰器"""

    def __init__(self, func):
        """__init__()等同于装饰器的外部函数

        func: 传递函数，必须有。代表传递函数层。
        """

        print("@{}装饰器的外部函数只为{}()函数启动一次".format(WithoutParams.__name__, func.__name__))
        self._func = func

    def __call__(self, *args, **kwargs):
        """__call__()中定义装饰器"""

        # 装饰器功能定义
        # 不需要@wraps(func)，因为基于类实现的装饰器没有嵌套函数。
        print("@{}装饰器的内部函数被{}()函数调用".format(self.__class__, self._func.__name__))
        print("args:{}, kwargs:{}".format(args, kwargs))
        self.extra_func()

        # 调用被修饰函数。
        self._func(*args, **kwargs)
        return None

    def extra_func(self):
        print("增加功能")


class WithParams(object):
    """基于类实现的带参数的装饰器"""

    def __init__(self, msg, level='INFO'):
        # 参数传递层
        self.msg = msg
        self.level = level

    def __call__(self, func):
        print("@{}装饰器的外部函数只为{}()函数启动一次".format(self.__class__, func.__name__))

        def wrapper(*args, **kwargs):
            print("@{}装饰器的内部函数被{}()函数调用".format(self.__class__, func.__name__))
            print("args:{}, kwargs:{}".format(args, kwargs))
            self.extra_func()
            func(*args, **kwargs)

        return wrapper

    def extra_func(self):
        print("增加功能")

# @WithoutParams
# def func4(text, age):
#     print("执行函数:", text, age)
#
#
# @WithParams(msg="hello")
# def func5(text, age):
#     print("执行函数:", text, age)
#
# func4("huxiajie", 18)
# func5("huxiajie", 18)
