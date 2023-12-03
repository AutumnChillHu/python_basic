# -*- coding: utf-8 -*-

class ClassStruct():
    class_var = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        local_var = "local_var"
        print(local_var)
        ClassStruct.class_var.append("__init__")

    def show(self):
        print("show")
        ClassStruct.static_method()

    @staticmethod
    def static_method():
        ClassStruct.class_var.append("static_method")
        ClassStruct.static_method2()
        ClassStruct.class_method2()

    @staticmethod
    def static_method2():
        ClassStruct.class_var.append("static_method2")

    @classmethod
    def class_method(cls):
        cls.class_var.append("class_method")
        cls.static_method2()
        cls.class_method2()

    @classmethod
    def class_method2(cls):
        cls.class_var.append("class_method2")


if __name__ == "__main__":
    obj = ClassStruct(1, 2)
    # print(obj.class_var, ClassStruct.class_var)
    obj1 = ClassStruct(1, 2)
    # print(obj.class_var, ClassStruct.class_var)
    # obj.static_method()
    # print(obj.class_var, ClassStruct.class_var)
    # ClassStruct.static_method()
    # print(obj.class_var, ClassStruct.class_var)

    obj.class_method()
    print(obj.class_var, ClassStruct.class_var)
    ClassStruct.class_method()
    print(obj.class_var, ClassStruct.class_var)

    # obj.static_method()
    # print(obj.class_var)
    # ClassStruct.static_method()
    # print(obj.class_var)
    #
    # obj1 = ClassStruct(1, 2)
    # ClassStruct.static_method()
    # print(obj1.class_var)
