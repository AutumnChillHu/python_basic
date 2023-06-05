# -*- coding: utf-8 -*-

"""this is the template about how code is organized

"""

# todo:多个import,分组？from import 放哪儿？
import sys


class Student(object):
    """
    A Student is an object used to provide students'information.

    Methods:

    update() -- student info
    graduate() -- return if already gratuated

    Attributes:

    name -- the student's name
    gender -- felmale or male
    """

    def __init__(self, *args, **kwargs):
        pass


    def update(self, *args, **kwargs):
        """ updates student info. """
        pass

    def graduate(self, name):
        """ return if already gratuated.
        these doc can be viewd by graduate.__doc__"""

        print(name)
        return True

    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gender = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


if __name__ == "__main__":
    pass
