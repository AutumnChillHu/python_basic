# -*- coding: utf-8 -*-
"""
-实现多线程的2种方式：
    1.threading.Thread类
    2.继承threading.Thread类

-线程的2种锁：
    1.Lock类
    2.RLock类
"""

import threading


def run(num):
    print("线程开始run{}>>> thread_name={}".format(num, threading.current_thread().name))
    time.sleep(4)
    print("线程结束run{}>>> thread_name={}".format(num, threading.current_thread().name))


"""实现多线程-方式1：threading.Thread类"""
from threading import Thread
import time


def new_threading():
    threading_list = []
    for i in range(5):
        # Thread(target=run, args=(i,))：初始化线程。
        #   -target：绑定启动线程时需要执行的方法。
        #   -args：以元组形式传递run()需要的的参数。
        #   -daemon：主动指定是否为守护线程True/False。意味着程序必须要等待守护线程结束后才能退出。
        #            默认为None，意味着new_thread=current_thread().daemon。
        #            通常当前线程是主线程，主线程不是守护线程，main_thread.daemon=False，由主线程创建的线程都不是守护线程。
        threading_list.append(Thread(target=run, args=(i,)))

        # 启动线程
        threading_list[i].start()

    # 下面介绍几种线程常用方法
    # join([timeout])：阻塞当前线程，直至thread终结。
    #   -可能是正常终结/抛出异常，线程不存活。
    #   -可能是超时终结，线程会仍然存活。
    threading_list[0].join()
    # is_alive()：
    #   -返回True：当run()方法刚开始直到run()方法刚结束。
    #   -返回False：run()方法结束后，无论以任何方式结束，正常结束or异常抛出
    threading_list[0].is_alive()


"""实现多线程-方式2：继承threading.Thread类"""


class MyThread(Thread):
    """只能重载Threading类的__init__()和run()"""

    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        print("线程开始run{}>>> thread_name={}".format(self.num, threading.current_thread().name))
        time.sleep(4)
        print("线程结束run{}>>> thread_name={}".format(self.num, threading.current_thread().name))


"""线程锁-方式1：Lock"""
from threading import Lock


def lock_threading():
    num = 0
    lock = Lock()
    for i in range(5):
        th = Thread(target=run_lock, args=(num,))
        # lock.acquire([,blocking=True][,timeout=-1])：上锁
        #   -blocking: 默认为True，阻塞直到获取到锁的使用权，然后锁定并返回True。指定False时，将不会发生阻塞。
        #   -timeout: 仅适用于阻塞模式，即blocking=True。
        #             指定最长阻塞时间，超时返回False；默认为-1时，表示无限等待。
        lock.acquire()

        th.start()

        # lock.release()：释放锁。
        #   当无法确保能获取到锁的使用权时，请使用if-else结构。防止release()报错"RuntimeError: release unlocked lock"
        lock.release()


def run_lock(num):
    num += 1
    time.sleep(1)
    num += 1


"""线程锁-方式2：RLock
1. RLock是递归锁Recursion Lock：可以重复多次上锁。
2. RLock内部维护 self._block 和 self._count。
   self._block是一个Lock()。
   self._count记录acquire的次数。资源可以被多次require，只有线程所有的acquire都被release，其他的线程才能获得资源。
"""
from threading import RLock


def rlock_threading():
    num = 0
    rlock = RLock()
    for i in range(5):
        Thread().start()


def run_rlock(rlock):
    print("{} start".format("是的"))
    global num_Rlock

    # 上锁：Rlock.acquire([blocking=True, ][timeout=-1])
    # 参数含义同lock.acquire()：blocking默认为True，timeout默认为-1。
    # 对于RLock，能获得锁的使用权=>锁空闲=>没有任何一个线程使用锁，全部释放。
    rlock.acquire()

    num_Rlock += 1
    time.sleep(0.5)
    num_Rlock += 1
    print("{} num_Rlock = {}".format("黑寡妇", num_Rlock))

    # 重复上锁
    rlock.acquire()
    rlock.release()
    rlock.release()


"""死锁-场景1：因程序设计，导致某些情况下没有执行释放锁的语句，导致其他线程无法再使用资源。"""

deadlock_unreleased = Lock()
deadlock_unreleased_list = [1, 2, 3]


def new_deadlock_unreleased(index):
    deadlock_unreleased.acquire()
    if index >= len(deadlock_unreleased_list) or index < 0:
        print("wrong index")
        return False
    print(deadlock_unreleased_list[index])
    deadlock_unreleased.release()
    return True


if __name__ == "__main__":
    # 主线程
    print(threading.current_thread().name, threading.current_thread().daemon)

    # 实现多线程
    # new_threading()

    # 线程锁
    # lock_threading()
    # rlock_threading()

    # 死锁举例
    # new_death_lock()
