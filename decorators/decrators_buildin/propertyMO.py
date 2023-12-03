# -*- coding: utf-8 -*-

class Employee(object):

    def __init__(self):
        self.__salary = 10000  # 私有属性，外部无法访问

    @property
    def salary(self):
        """通过@property 让外部可以读私有属性（obj.salary）"""
        return self.__salary

    @salary.setter
    def salary(self, increment):
        """通过@salary.setter 让外部可以写私有属性（obj.salary=100）"""
        if self.__salary + increment < 5000:
            self.__salary = 5000
        elif self.__salary + increment > 20000:
            self.__salary = 20000
        else:
            self.__salary += increment

    @salary.deleter
    def salary(self):
        """通过@salary.deleter 让外部可以删除私有属性（del obj.salary）"""
        self.__salary = 0


if __name__ == "__main__":
    employee = Employee()
    print(employee.salary)
    employee.salary = 150
    print(employee.salary)
    del employee.salary
    print(employee.salary)
