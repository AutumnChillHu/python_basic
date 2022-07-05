# -*- coding: utf-8 -*-

class Stu(object):

    def __init__(self):
        self.name = "jjj"
        self.gender = "male"

    def __eq__(self, other):  # real signature unknown
        """ Return self==value. """
        return self.name == other.name and self.gender == other.gender

    def __hash__(self):  # real signature unknown
        """ Return hash(self). """
        return hash((self.name, self.gender))

    def pr(self):
        return True


if __name__ == "__main__":
    d = {"name": "Alex", "age": 18, "gender": "Man"}
    stu1 = Stu()
    stu2 = Stu()
    print(stu2 is stu1, stu2 == stu1, hash(stu1)==hash(stu2))
    d1 = str
    s = "2222"
    print(hash(s))
    s += "2"
    print(hash(s), s.__hash__())
    print(hash(d["name"]), hash(d["name"]) % 2, hash(d["name"]) % 3, hash(d["name"]) % 4)
    print(hash(d["age"]), hash(d["age"]) % 2, hash(d["age"]) % 3, hash(d["age"]) % 4)
    print(hash(d["gender"]), hash(d["gender"]) % 2, hash(d["gender"]) % 3, hash(d["gender"]) % 4)
    l = [1, 2, 3]
    print(hash(l[2]), id(l))
    d1 = {"name": "Alex", "gender": "Man", "age": 18}
    d2 = {"age": 18, "gender": "Man", "name": "Alex", }
    x = list
    print(d1 == d2, d1 == d)
    l1 = [1, 2, 3]
    l2 = [1, 2, 3]
    l3 = [3, 2, 1]
    print(l1 == l2)
    x, y = 0, False
    print(x == y, hash(0) == hash("False"))
