# -*- coding: utf-8 -*-
"""
-实现多线程：
    1. 使用 threading.Thread类 创建线程。
    2. 使用 继承threading.Thread类 的自定义类 创建线程。

-线程锁：
    1. threading.Lock类
    2. threading.RLock类
"""
import random
import threading
import time


def run(seconds):
    print("线程开始run>>>thread_name={} args={}".format(threading.current_thread().name, seconds))
    time.sleep(seconds)
    print("线程结束run>>>thread_name={} args={}".format(threading.current_thread().name, seconds))


"""实现多线程-1. 使用 threading.Thread类 创建线程。"""
from threading import Thread


def new_threading():
    threading_list = []
    datas = [random.randint(0, 10) for _ in range(5)]  # random.randint(a, b) 返回[a, b]区间内的一个随机整数

    # Thread(target=run, args=(i,) [,daemon=False])：初始化线程。
    #   -target：绑定启动线程时需要执行的run()方法。
    #   -args：以元组形式传递run()需要的的参数。
    #   -daemon：指定是否为守护线程True/False。默认为None，意味着new_thread.daemon=current_thread().daemon。
    for data in datas:
        th = Thread(target=run, args=(data,))
        threading_list.append(th)
        # 异步启动线程
        th.start()

    # join([timeout])：默认timeout为None，意味着永久等待。
    #   -阻塞当前线程，直至thread终结或者超时，共3种情况：1)thread run正常执行结束。2)thread run异常结束。3)thread未结束，等待超时。
    threading_list[-1].join(60)

    # is_alive()：判断线程是否在运行
    #   -返回True：当run()方法刚开始直到run()方法刚结束。
    #   -返回False：run()方法结束后，无论run()正常/异常结束都算。
    # 调用join()之后，再调用is_alive()，可以捕获join()后线程仍然存活的情况，如join()等待超时。
    if threading_list[-1].is_alive():
        raise RuntimeError("thread could not stop running")
    print("在threading_list[-1]结束的条件下，做一些运算。")


"""实现多线程-2. 使用 继承threading.Thread类 的自定义类 创建线程。"""


class MyThread(Thread):
    """重载Threading类的__init__()和run()"""

    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        print("线程开始run>>>thread_name={} args={}".format(threading.current_thread().name, self.num))
        time.sleep(self.num)
        print("线程结束run>>>thread_name={} args={}".format(threading.current_thread().name, self.num))


"""线程锁-1. threading.Lock类"""
from threading import Lock


def lock_bywith():
    """使用with语句释放锁"""
    li = []
    lock = Lock()
    for i in range(5):
        Thread(target=run_lock_bywith, args=(li, lock)).start()
    print("li: {}".format(li))


def run_lock_bywith(li, lock):
    with lock:
        li.append(threading.current_thread().name)
        print("thread:{}, li:{}".format(threading.current_thread().name, li))
        # 如果不上锁，print执行前会让出GIL，导致print前后li[-1]不一致。
        li[-1] += "mo"
        print("thread:{}, li:{}".format(threading.current_thread().name, li))


def lock_byfinally():
    """使用finally语句释放锁"""
    li = []
    lock = Lock()
    for i in range(5):
        Thread(target=run_lock_finally, args=(li, lock)).start()
    while lock.locked():  # 获取锁的状态
        print("waiting for thread end")
        time.sleep(1)
    print("li: {}".format(li))


def run_lock_finally(li, lock):
    try:
        # acquire([,blocking=True][,timeout=-1])：上锁。
        #   -blocking: 默认为True。意味着如果已经是锁定状态，将阻塞当前线程直到锁被释放，然后立刻上锁。
        #   -timeout: 仅适用于blocking=True。指定最长阻塞时间，超时返回False；默认为-1时，表示无限等待。
        lock.acquire()
        li.append(threading.current_thread().name)
        print("thread:{}, li:{}".format(threading.current_thread().name, li))
        li[-1] += "mo"
        print("thread:{}, li:{}".format(threading.current_thread().name, li))
    finally:
        # release()：可以在任何线程释放，意味着acquire&release不需要出现在同一线程中。
        #           非锁定状态时，调用此方法会引发RuntimeError，保险起见可用if lock.locked()。
        lock.release()


"""线程锁-2. threading.RLock类"""
from threading import RLock

def adder(rlock, goods_list, add_list):
    """with语句"""
    for i in add_list:
        with rlock:
            goods_list.append(i)
            print("add 1 item {}".format(goods_list))
            time.sleep(0.5)
def remover(rlock, goods_list, remove_cnt):
    """finally语句"""
    while remove_cnt > 0:
        try:
            rlock.acquire()
            item = goods_list.pop()
            print("remove 1 item {}, {}".format(item, goods_list))
            remove_cnt -= 1
        except IndexError:
            print("not enough goos to remove {}".format(goods_list))
            break  # 如果这里用return语句将不会执行finally语句。
        finally:
            rlock.release()
        time.sleep(1)

def rlock():
    goods_list = []
    rlock = RLock()
    th_add = Thread(target=adder, args=(rlock, goods_list, [1, 2, 3, 4, 5, 6, 7]))
    th_remove = Thread(target=remover, args=(rlock, goods_list, 8))
    th_add.start()
    th_remove.start()
    th_add.join()
    th_remove.join()


if __name__ == "__main__":
    # 主线程
    # print(threading.current_thread().name, threading.current_thread().daemon)

    # 实现多线程
    # new_threading()

    # 线程锁
    # lock_bywith()
    # lock_byfinally()
    # rlock()

    rlock()

    pass
