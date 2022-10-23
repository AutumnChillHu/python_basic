# -*- coding: utf-8 -*-

"""
带参数的装饰器：需要再包一层

from functools import wraps

def log_with_param(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s():' % func.__name__)
            print('args = {}, kwargs = {}'.format(args, kwargs))
            print('log_param = {}'.format(text))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_with_param("param")
def test_with_param(p):
    print(test_with_param.__name__)
//调用
test_with_param(p="hxj")
//结果
call test_with_param()
args = (), kwargs = {'p': 'hxj'}
log_param = param
test_with_param
"""

"""
通过类实现装饰器

class Decrator():
    def __init__(self, func):
        self._func = func

    //class decorator执行装饰器就是执行__call__函数
    def __call__(self, *args, **kwargs):
        print('class decorator start')
        print(self._func.__name__)  # 原函数
        self.more_func()
        self._func(*args, **kwargs)  # 原函数
        print('class decorator ending')

    def more_func(self):
        print("增加功能")

@Decrator
def func_name(name, age):
    print("执行函数", name, age)

func_name("huxiajie", 23)

//结果
class decorator start
func_name
增加功能
执行函数 hxj 23
class decorator ending

不再需要@wraps(func)，因为没有嵌套函数
"""


if __name__ == "__main__":
    pass
