# -*- coding: utf-8 -*-
"""
准则：优秀实用主义。实用且推荐写法。
"""


def if_has_key(key, d):
    if key in d:
        return True


def if_has_value(d):
    """判断字典中是否包含value/key-value"""

    # 当key不存在时，d.get()返回None，但是如果d["key"]为空，也不会执行if语句
    # d["key"]会报KeyError。
    if d.get("key"):
        return True

    # dict是否包含value
    if "value" in d.values():
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


if __name__ == "__main__":
    d = {"name": "mo", "age": 25, "gender": None}
