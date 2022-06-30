# -*- coding: utf-8 -*-


import gc
import readline
import sys

if __name__ == "__main__":
    l1, l2 = [1], [2]
    l1.append(l2)
    l2.append(l1)
    l1 = [4]
    l2 = [4]
    print(gc.get_threshold())
    # print(gc.get_stats())
    for i in gc.get_stats():
        print(i)
    print(gc.get_count())
    print(gc.garbage)
