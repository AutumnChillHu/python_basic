# -*- coding: utf-8 -*-
import time


def timer():
    """统计执行时间"""
    time_start = time.time()
    time.sleep(5)
    time_end = time.time()

    # 按秒输出
    print("程序执行时间为", time_end - time_start, "秒")
    return None


if __name__ == "__main__":
    pass
