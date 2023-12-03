# -*- coding: utf-8 -*-
'''装饰器特性说明'''

from functools import wraps


def study(func):
    """this is study()"""
    print("@{}装饰器的外部函数只为{}()函数启动一次".format(study.__name__, func.__name__))

    @wraps(func)
    def wrapper(*args, **kwargs):
        """this is wrapper()"""
        # 装饰器内部修改不可变对象
        if "age" in kwargs:
            kwargs["age"] += 1
        # 装饰器内部原地修改可变对象
        if "family" in kwargs:
            kwargs["family"].append("MO")
        print("@{}装饰器的内部函数被{}()函数调用".format(study.__name__, wrapper.__name__))
        print("args:{}, kwargs:{}\ndoc: {}".format(args, kwargs, wrapper.__doc__))
        return func(*args, **kwargs)

    print("@{}装饰器的外部函数只为{}()函数启动一次完毕".format(study.__name__, func.__name__))
    return wrapper


@study
def func(name, age, family):
    """this is func()"""

    name += "MO"
    age += 1
    family.append("MO")
    print("run {}(), name:{}, age:{}, family:{}".format(func.__name__, name, age, family))


print("+++++++++++++++++++++++++")


@study
def func_baby(name, age, family):
    """this is func_baby()"""

    name += "MO"
    age += 1
    family.append("MO")
    print("run {} {} {} {}".format(func.__name__, name, age, family))


print("+++++++++++++++++++++++++")
func(name="hxj", age=18, family=[7, 8, 9])
print("+++++++++++++++++++++++++")
func("hxj", 18, [7, 8, 9])
print("+++++++++++++++++++++++++")
func_baby("hxj", 18, [7, 8, 9])

if __name__ == "__main__":
    pass
