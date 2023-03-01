# -*- coding: utf-8 -*-
"""
实现多线程的2种方式：
    1.threading.Thread类
    2.继承threading.Thread类

多线程安全-上锁的2种方式：
    1.Lock类
    2.RLock类

死锁的2种常见场景：
    1.因程序设计，导致某些情况下没有执行释放锁的语句，导致其他线程无法再使用资源。
    2。

"""
import os
import threading

"""实现多线程-方式1：threading.Thread类"""
from threading import Thread
import time


def threading_run(n):
    print("start threading task：{}".format(n))
    time.sleep(2)

    # threading模块提供获取当前线程的方法
    print("ending threading task：{}".format(threading.current_thread().getName()))


def new_threading():
    threading_list = []
    for i in range(5):
        # 初始化线程：Thread(target=func_name, args=(i,))
        # target：绑定启动线程时需要执行的方法，相当于绑定run()方法。
        # args：以元组形式传递target的参数。
        threading_list.append(Thread(target=threading_run, args=(i,)))

        # 将threading_list[4]线程设置为守护线程：表示进程退出的时，必须要等待守护线程结束后才能退出。
        if i == 4:
            threading_list[i].setDaemon(True)

        # 启动线程
        threading_list[i].start()

        # 将threading_list[0]线程设置为同步线程，即只有当前线程执行完毕，才允许主线程继续向下执行或结束。相当于单线程。
        # join()必须用在start()之后。
        if i == 0:
            threading_list[i].join()


"""实现多线程-方式2：继承threading.Thread类"""


class MyThread(Thread):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def run(self):
        """重写run方法"""
        print("start threading task：{}".format(self.msg))
        time.sleep(3)
        print("end threading task：{}".format(self.msg))


def new_mythreading():
    threading_list = []
    for i in range(5):
        threading_list.append(MyThread(i))
        threading_list[i].start()


"""线程安全-上锁-方式1：Lock
1. Lock()需要是全局变量，需要是多个线程共享。
2. Lock()是对共享数据空间进行上锁。
"""
from threading import Lock

num_lock = 0
lock = Lock()


class MyLockThread(Thread):
    def run(self):
        global num_lock

        # 上锁：lock.acquire([blocking=True, ][timeout=-1])
        # blocking: 默认为True，阻塞直到获取到锁的使用权，然后锁定并返回True。指定False时，将不会发生阻塞。
        # timeout: 仅适用于阻塞模式，即blocking=True。
        #          指定最长阻塞时间，超时返回False；默认为-1时，表示无限等待。
        lock.acquire()

        num_lock += 1
        time.sleep(0.5)
        num_lock += 1
        print("{} num_lock = {}".format(self.name, num_lock))

        # 释放锁。
        # 当无法确保能获取到锁的使用权时，请使用if-else结构。防止release()报错"RuntimeError: release unlocked lock"
        lock.release()


def lock_threading():
    for i in range(5):
        MyLockThread().start()


"""线程安全-上锁-方式2：RLock
1. RLock是递归锁Recursion Lock：可以重复多次上锁。
2. RLock内部维护 self._block 和 self._count。
   self._block是一个Lock()。
   self._count记录acquire的次数。资源可以被多次require，只有线程所有的acquire都被release，其他的线程才能获得资源。
"""
from threading import RLock

num_Rlock = 0
Rlock = RLock()


class MyRLockThread(Thread):
    def run(self):
        print("{} start".format(self.name))
        global num_Rlock

        # 上锁：Rlock.acquire([blocking=True, ][timeout=-1])
        # 参数含义同lock.acquire()：blocking默认为True，timeout默认为-1。
        # 对于RLock，能获得锁的使用权=>锁空闲=>没有任何一个线程使用锁，全部释放。
        Rlock.acquire()

        num_Rlock += 1
        time.sleep(0.5)
        num_Rlock += 1
        print("{} num_Rlock = {}".format(self.name, num_Rlock))

        # 重复上锁
        Rlock.acquire()
        Rlock.release()
        Rlock.release()


def rlock_threading():
    for i in range(5):
        MyRLockThread().start()


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
    # 实现多线程-方式1：threading.Thread类
    new_threading()
    # 实现多线程-方式2：继承threading.Thread类
    # new_mythreading()
    # 线程安全-上锁-方式1：Lock类
    # lock_threading()
    # 线程安全-上锁-方式2：RLock类
    # rlock_threading()

    # new_death_lock()
