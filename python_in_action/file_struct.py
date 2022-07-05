# -*- coding: utf-8 -*-

"""this is the template on how the code is organized

"""

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

    def update(self, *args, **kwargs):
        """ updates student info. """
        pass

    def graduate(self, name):
        """ return if already gratuated. """
        print(name)
        return True

    def __init__(self, *args, **kwargs):
        pass

    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gender = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


if __name__ == "__main__":
    pass
