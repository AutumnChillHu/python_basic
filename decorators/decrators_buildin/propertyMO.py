# -*- coding: utf-8 -*-

class Employee(object):

    def __init__(self):
        self.__salary = 10000

    @property
    def salary(self):
        """通过@property 可以让方法变属性，而且是只读属性"""
        return self.__salary

    @salary.setter
    def salary(self, increment):
        """通过@salary.setter 可以进行修改校验"""
        if self.__salary + increment < 5000:
            self.__salary = 5000
        elif self.__salary + increment > 20000:
            self.__salary = 20000
        else:
            self.__salary += increment

    @salary.deleter
    def salary(self):
        self.__salary = 0


if __name__ == "__main__":
    employee = Employee()
    print(employee.salary)
    employee.salary = 150
    print(employee.salary)
    del employee.salary
    print(employee.salary)
