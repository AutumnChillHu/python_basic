# -*- coding: utf-8 -*-
"""分别基于函数、类实现装饰器，实现无参数、带参数的装饰器。"""

from functools import wraps


def without_params(func):
    """基于函数实现不带参数的装饰器"""
    # 传递函数层
    print("@{}装饰器的 传递函数层 为{}()函数只启动一次".format(without_params.__name__, func.__name__))

    @wraps(func)
    def wrapper(*args, **kwargs):
        # 装饰器具体实现层
        result = func(*args, **kwargs)  # 直接执行了
        print("@{}装饰器的具体实现层被{}()函数调用".format(without_params.__name__, wrapper.__name__))
        return result
        # return func(*args, **kwargs) #直接返回

    print("@{}装饰器的 传递函数层 为{}()函数启动完毕".format(without_params.__name__, func.__name__))

    return wrapper


def with_params(li, text="hello"):
    """基于函数实现带参数的装饰器"""
    # 传递参数层
    print("@{}装饰器的 传递参数层 只启动一次".format(with_params.__name__))

    def pass_func(func):
        # 传递函数层
        print("@{}装饰器的 传递函数层 为{}()函数只启动一次".format(with_params.__name__, func.__name__))

        @wraps(func)
        def wrapper(*args, **kwargs):
            """装饰器具体实现层"""
            print("@{}装饰器的 具体实现层 被{}()函数调用".format(with_params.__name__, wrapper.__name__))
            print('args:{}, kwargs:{}'.format(args, kwargs))
            print('params:{}, {}'.format(text, li))
            return func(*args, **kwargs)

        print("@{}装饰器的 传递函数层 为{}()函数启动完毕".format(with_params.__name__, func.__name__))
        return wrapper

    print("@{}装饰器的 传递参数层 启动完毕".format(with_params.__name__))
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

# @with_params([1])
# @with_params([1, 2, 3], "hello world")
# def func3(name):
#     name += "MO"
#     return None


# func1("hxj")
# func2("hxj")
# func3("hxj")


class WithoutParams():
    """基于类实现的不带参数的装饰器"""

    def __init__(self, func):
        """__init__()：等同于装饰器的函数传递层，要带func参数"""
        self._func = func
        print("@{}装饰器的 传递函数层 为{}()函数只启动一次".format(WithoutParams.__name__, self._func.__name__))

    def __call__(self, *args, **kwargs):
        """__call__()：等同于装饰器的具体实现层"""

        # 不需要@wraps(func)了
        self.extra_func()
        result = self._func(*args, **kwargs)
        print("@{}装饰器的具体实现层被{}()函数调用".format(without_params.__name__, self._func.__name__))
        return result
        # return self._func(*args, **kwargs) #直接返回

    def extra_func(self):
        print("增加功能")


class WithParams():
    """基于类实现的带参数的装饰器"""

    def __init__(self, msg, level='INFO'):  # 不能接收func，会报错，说少传了一个参数。
        # 参数传递层
        self.msg = msg
        self.level = level
        print("@{}装饰器的 参数传递层 为函数只启动一次".format(WithParams.__name__))

    def __call__(self, func):
        # 函数传递层
        print("@{}装饰器的 传递函数层 为{}()函数只启动一次".format(WithParams.__name__, func.__name__))

        def wrapper(*args, **kwargs):
            # 装饰器具体实现层
            print("@{}装饰器的 具体实现层 被{}()函数调用".format(self.__class__, func.__name__))
            print("args:{}, kwargs:{}".format(args, kwargs))
            self.extra_func()
            result = func(*args, **kwargs)
            return result
            # return func(*args, **kwargs)

        return wrapper

    def extra_func(self):
        print("增加功能")


# @WithoutParams
# def func4(text, age):
#     print("执行函数:", text, age)
#
#
@WithParams(msg="hello")
def func5(text, age):
    print("执行函数:", text, age)

#
# func4("huxiajie", 18)
# func5("huxiajie", 18)
