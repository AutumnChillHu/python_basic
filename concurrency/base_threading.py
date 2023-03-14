# -*- coding: utf-8 -*-
"""
-实现多线程：
    1.threading.Thread类 & 继承threading.Thread类

-线程锁：
    1.Lock类
    2.RLock类

-死锁：
    1.哲学家就餐问题
"""
import random
import threading
import time


def run(seconds):
    print("线程开始run>>>thread_name={} args={}".format(threading.current_thread().name, seconds))
    time.sleep(seconds)
    print("线程结束run>>>thread_name={} args={}".format(threading.current_thread().name, seconds))


"""实现多线程：threading.Thread类 & 继承threading.Thread类"""
from threading import Thread


def new_threading():
    threading_list = []
    datas = [random.randint(0, 10) for i in range(5)]
    # Thread(target=run, args=(i,) [,daemon=False])：初始化线程。
    #   -target：绑定启动线程时需要执行的方法。
    #   -args：以元组形式传递run()需要的的参数。
    #   -daemon：主动指定是否为守护线程True/False。默认为None，意味着new_thread.daemon=current_thread().daemon。
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
    # 调用join()之后，再调用is_alive()，可以捕获join()后线程仍然存活的情况。
    if threading_list[-1].is_alive():
        raise RuntimeError("thread could not stop running")
    print("在threading_list[-1]结束的条件下，做一些运算。")


class MyThread(Thread):
    """只能重载Threading类的__init__()和run()"""

    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        run(self.num)


"""线程锁：Lock"""
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

    while lock.locked():
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
        # release()：可以在任何线程释放，意味着acquire&release不需要出现在统一线程中。
        #           非锁定状态时，调用此方法会引发RuntimeError，保险起见可用if lock.locked()。
        lock.release()


"""线程锁：RLock"""
from threading import RLock


class Box(object):
    def __init__(self):
        self._rlock = Lock()
        self.count = 0

    def execute(self, num):
        self._rlock.acquire()
        self.count += num
        self._rlock.release()

    def add(self):
        # 在release()之前调用了一个也需要锁的方法，所以需要RLock()
        self._rlock.acquire()
        self.execute(1)
        self._rlock.release()

    def remove(self):
        # 调用了一个也需要锁的方法
        self._rlock.acquire()
        self.execute(-1)
        self._rlock.release()


def adder(box, items):
    while items > 0:
        print("add 1 item in the box")
        box.add()
        time.sleep(1)
        items -= 1


def remover(box, items):
    while items > 0:
        print("remove 1 item in the box")
        box.remove()
        time.sleep(2)
        items -= 1


def rlock():
    box = Box()
    items = 5
    th_add = Thread(target=adder, args=(box, items))
    th_remove = Thread(target=remover, args=(box, items))
    th_add.start()
    th_remove.start()

    print("now we have {} in box".format(box.count))
    th_add.join()
    print("after th_add.join() we have {} in box".format(box.count))
    th_remove.join()
    print("after th_remove we have {} in box".format(box.count))


"""死锁：
为
因程序设计，导致某些情况下没有执行释放锁的语句，导致其他线程无法再使用资源。try——finally/with"""

deadlock_unreleased = Lock()
deadlock_unreleased_list = [1, 2, 3]

from concurrency.tool_sortlocks import acquire


def deadlock_unreleased(index):
    deadlock_unreleased.acquire()
    if index >= len(deadlock_unreleased_list) or index < 0:
        print("wrong index")
        return False
    print(deadlock_unreleased_list[index])
    deadlock_unreleased.release()
    return True


"""死锁-场景2：一个线程中尝试获取多个lock
经典问题：哲学家就餐问题
"""


def philosopher():
    people = 5
    chopsticks_locks = [threading.Lock() for i in range(people)]
    for i in range(people):
        Thread(target=eat, args=(chopsticks_locks[i], chopsticks_locks[(i + 1) % people])).start()


def eat(left_stick, right_stick):
    while True:
        print("{} applying".format(threading.current_thread().name))
        # with left_stick:
        #     with right_stick:
        #         print("{} eating".format(threading.current_thread().name))
        #         time.sleep(3)
        with acquire(left_stick, right_stick):
            print("{} eating".format(threading.current_thread().name))
            time.sleep(3)


if __name__ == "__main__":
    # 主线程
    # print(threading.current_thread().name, threading.current_thread().daemon)

    # 实现多线程
    # new_threading()

    # 线程锁
    # lock_byfinally()
    # lock_bywith()
    # rlock()

    # 死锁
    # philosopher()
    pass
