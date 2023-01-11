# -*- coding: utf-8 -*-


global d


def has_dict():
    """判断字典中是否包含key/value/key-value"""

    # dict是否包含key
    if "name" in d:
        print("in dict")
        return True

    # if "name" in d.keys():
    #     print("in dict.keys()")
    #     return True

    # dict是否包含value
    if "mo" in d.values():
        print("in dict.values()")
        return True

    # dict是否包含key-value
    if ("name", "mo") in d.items():
        print("in d.items()")
        return True

    return False


def traversal_dict():
    """遍历字典"""

    # 遍历键值对
    for i in d.items():
        # 元组形式返回
        print(i)

    for k, v in d.items():
        print(k, v)

    # 遍历keys
    for i in d:
        print(i)

    # for i in d.keys():
    #     print(i)

    # 遍历d.values()
    for i in d.values():
        print(i)


def delete_dict():
    """删除字典元素"""

    # 删除key为age的键值对，返回value
    print(d.pop("age"))
    # key不存在：KeyError
    # print(d.pop("habit"))

    # 删除最后一对键值对，以元组形式返回被删除的键值对
    print(d.popitem())
    # 空字典：KeyError: dictionary is empty'
    # print(dict().popitem())

if __name__ == "__main__":
    d = {"name": "mo", "age": 25, "gender": "female"}
