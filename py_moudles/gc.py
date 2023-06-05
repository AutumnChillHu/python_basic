# -*- coding: utf-8 -*-
"""This is the example module.

This module does stuff.
"""

import gc


def methods():
    # 返回gc三代回收阈值 (threshold0, threshold1, threshold2)
    print(gc.get_threshold())

    # 返回gc当前回收计数
    print(gc.get_count())

    # 返回包含三个字典对象的列表
    # 每个字典分别包含对应代的从解释器开始运行的垃圾回收统计数据。目前每个字典包含以下内容：
    # collections：该代执行回收的次数；
    # collected  ：该代中被回收的对象总数；
    # uncollectable：该代不可回收对象列表：又不可达而又无法被释放的对象；会被移动到garbage列表中。
    print(gc.get_stats())


def attrs():
    # 不可回收对象列表：又不可达而又无法被释放的对象。
    print(gc.garbage)


if __name__ == "__main__":
    methods()
    attrs()
