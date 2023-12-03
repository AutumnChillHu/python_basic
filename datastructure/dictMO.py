# -*- coding: utf-8 -*-

def if_has_key(key, d):
    if key in d:
        return True


def if_has_value(d):
    """判断字典中是否包含value/key-value"""

    # key不存在时，d["key"]会报KeyError，d.get("key")返回None。
    if d.get("key"):
        return True

    # dict是否包含key-value
    if ("key", "value") in d.items():
        return True

    return False


def traversal_dict(d):
    """遍历字典"""

    # 遍历keys
    for i in d:
        print(i, d[i])

    # 遍历键值对
    for k, v in d.items():
        print(k, v)
    for i in d.items():
        # 元组格式
        print(i)


def delete_dict(d):
    """删除字典元素"""

    # 删除键值对，返回value。
    # key不存在/空字典，报KeyError。
    print(d.pop("key"))

    # 删除最后一对键值对，以元组格式返回被删键值对。
    # 空字典，报KeyError。
    print(d.popitem())


def sort_dict(d={"z": 1, "a": 100, "t": 50}):
    # 1.对key排序，默认情况。
    print(sorted(d), sorted(d.keys()))
    # 2.对value排序
    print(sorted(d.values()))
    # 不影响原对象
    print(d)


if __name__ == "__main__":
    d = {"name": "mo", "age": 25, "gender": None}
    d2 = {"age": 25, "name": "mo", "g¬ender": None}
    # print(d == d2)
    sort_dict()
