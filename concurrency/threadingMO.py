# -*- coding: utf-8 -*-
"""
-实现多线程的2种方式：
    1.threading.Thread类
    2.继承threading.Thread类

-线程的2种锁：
    1.Lock类
    2.RLock类

-多线程与单线程提效对比：
    1.斐波那契数列
    2。阶乘与累加函数
"""

import threading
import time

from decorators.timer import timer


def run_long(msg):
    print(
        "线程开始run>>> fun_name={} thread_name={} args={}".format(run_long.__name__, threading.current_thread().name, msg))
    time.sleep(4)
    print(
        "线程结束run>>> fun_name={} thread_name={} args={}".format(run_long.__name__, threading.current_thread().name, msg))


def run_short(msg):
    print("线程开始run>>> fun_name={} thread_name={} args={}".format(run_short.__name__, threading.current_thread().name,
                                                                 msg))
    time.sleep(2)
    print("线程结束run>>> fun_name={} thread_name={} args={}".format(run_short.__name__, threading.current_thread().name,
                                                                 msg))


def run(seconds):
    print("线程开始run>>> fun_name={} thread_name={} args={}".format(__name__, threading.current_thread().name, seconds))
    time.sleep(seconds)
    print("线程结束run>>> fun_name={} thread_name={} args={}".format(__name__, threading.current_thread().name, seconds))


"""实现多线程-方式1：threading.Thread类"""
from threading import Thread


@timer
def new_threading():
    threading_list = []
    # Thread(target=run, args=(i,))：初始化线程。
    #   -target：绑定启动线程时需要执行的方法。
    #   -args：以元组形式传递run()需要的的参数。
    #   -daemon：主动指定是否为守护线程True/False。意味着程序必须要等待守护线程结束后才能退出。
    #            默认为None，意味着new_thread=current_thread().daemon。
    #            通常当前线程是主线程，主线程不是守护线程，main_thread.daemon=False，由主线程创建的线程都不是守护线程。（搞反了）
    # 一个线程可以被标记成一个“守护线程”。 这个标识的意义是，当剩下的线程都是守护线程时，整个 Python 程序将会退出。 初始值继承于创建线程。
    # 这个标识可以通过 daemon 特征属性或者 daemon 构造器参数来设置。
    threading_list.append(Thread(target=run_long, args=("task run_long",)))
    # threading_list.append(Thread(target=run_short, args=("task run_short",)))
    threading_list.append(Thread(target=run_short, args=("task run_short",), daemon=True))
    # todo：do some work

    for th in threading_list:
        # 启动线程
        th.start()

    # data = [i for i in range(10)]
    # for d in data:
    #     Thread(target=run, args=(d,)).start()

    # 下面介绍几种线程常用方法
    # join([timeout])：阻塞当前线程，直至thread终结。
    #   -可能是正常终结/抛出异常，线程不存活。
    #   -可能是超时终结，线程会仍然存活。
    # threading_list[0].join()
    # do sth join（）作为一种条件，而不是等待结束。
    # 此方法结束了，但主线程仍然会等待子线程执行完毕后再结束。线程一旦启动后，就开始独立地运行，知道run方法结束（除了daemon线程）
    # 解释器会一直保持运行，直到所有的非daemon线程都终止。（验证一下）

    # is_alive()：线程时是否还在运行
    #   -返回True：当run()方法刚开始直到run()方法刚结束。
    #   -返回False：run()方法结束后，无论以任何方式结束，正常结束or异常抛出
    # threading_list[0].is_alive()


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


"""线程锁-方式1：Lock
锁是被多线程共享的，无论线程发生什么意外，都需要正确释放，否则就会造成其他线程永久等待的问题。
    -1）要么用finally语句释放锁。
    -2）要么用with-as语句释放锁。
通过实践发现，with语句偶现上锁不成功的情况不够稳定，所以推荐finally。
"""
from threading import Lock


def lock_by_finally():
    """1）使用finally语句释放锁"""
    li = []
    lock = Lock()

    for i in range(5):
        th = Thread(target=run_lock_finally, args=(li, lock))
        # acquire([,blocking=True][,timeout=-1])：上锁。
        #   -blocking: 默认为True。意味着如果已经是锁定状态，将阻塞当前线程直到锁被释放，然后立刻上锁。
        #   -timeout: 仅适用于blocking=True。指定最长阻塞时间，超时返回False；默认为-1时，表示无限等待。
        lock.acquire()

        # 不支持重复调用锁，此处再次调用会引发没有release而永久等待锁的问题。
        # lock.acquire()

        th.start()

        # 此处调用release并起不到上锁的作用，因为start()异步返回。
        # lock.release()

    # 锁同步状态的例子 need better one only 状态 not变量
    while not lock.locked():
        print("waiting for thread end")
    print("li: {}".format(li))


def run_lock_finally(li, lock):
    # 不支持重复调用锁，此处再次调用也会引发没有release而永久等待锁的问题。
    # lock.acquire()

    try:
        li.append(threading.current_thread().name)
        print("thread:{}, li:{}".format(threading.current_thread().name,
                                        li))  # 如果不上锁，print语句执行前就会让出GIL，导致print前后li[-1]并不一致。
        li[-1] += "mo"
        print("thread:{}, li:{}".format(threading.current_thread().name, li))
    finally:
        # release()：可以在任何线程释放，意味着acquire&release不需要出现在统一线程中。
        #           非锁定状态时，调用此方法会引发RuntimeError，保险起见可用if lock.locked()。
        lock.release()


def lock_by_with():
    """2）使用with-as语句释放锁"""
    li = []
    for i in range(5):
        Thread(target=run_lock_with, args=(li,)).start()
    print("li: {}".format(li))


def run_lock_with(li):
    # 进入语句块时，acquire()会被调用。
    # 退出语句块时，release()会被调用。
    with Lock():
        li.append(threading.current_thread().name)
        print("thread:{}, li:{}".format(threading.current_thread().name, li))
        li[-1] += "mo"
        print("thread:{}, li:{}".format(threading.current_thread().name, li))


"""线程锁-方式2：RLock
递归锁是被多线程共享的，无论线程发生什么意外，都需要正确释放，否则就会造成其他线程永久等待的问题。
    -1）要么用finally语句释放锁。
    -2）要么用with-as语句释放锁。
"""
from threading import RLock


def rlock_by_finally():
    """1）使用finally语句释放锁"""
    li = []
    rlock = RLock()

    for i in range(5):
        th = Thread(target=run_rlock_by_finally, args=(li, rlock))
        # acquire([,blocking=True][,timeout=-1])：上锁。参数含义同lock.acquire()。
        #   -blocking: 默认为True。意味着如果已经是锁定状态，将阻塞当前线程直到锁被释放，然后立刻上锁。
        #   -timeout: 仅适用于blocking=True。指定最长阻塞时间，超时返回False；默认为-1时，表示无限等待。
        # 能获得锁的使用权=>锁空闲，锁递归级别=0.=>没有任何一个线程使用锁，全部释放。
        rlock.acquire()

        # 允许重复多次上锁，如果这个线程已经拥有锁，递归级别增加1，并立即返回不阻塞。如果其他线程拥有锁，阻塞等待后递归级别增加1
        rlock.acquire()

        th.start()

        rlock.release()
    print("li: {}".format(li))


def run_rlock_by_finally(li, rlock):
    # 允许重复多次上锁，如果这个线程已经拥有锁，递归级别增加1，并立即返回不阻塞。如果其他线程拥有锁，阻塞等待后递归级别增加1
    rlock.acquire()

    try:
        li.append(threading.current_thread().name)
        print("thread:{}, li:{}".format(threading.current_thread().name, li))
        li[-1] += "mo"
        print("thread:{}, li:{}".format(threading.current_thread().name, li))
    finally:
        # 此处的rlock只能在acquire()所在的线程被释放，这意味着acquire-release要在一个线程内要成对出现。
        # 只有当前线程拥有锁才能调用这个方法。如果锁被释放后调用这个方法，会引起RuntimeError异常。

        # 递归级别减1，只有减到零时，则将锁重置为非锁定状态
        # self._count记录acquire的次数。资源可以被多次require，只有线程所有的acquire都被release，其他的线程才能获得资源。
        rlock.release()
    print()


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
    new_threading()

    # 线程锁
    # lock_by_finally()
    # lock_by_with()
    # rlock_threading()

    # 死锁举例
    # new_death_lock()
