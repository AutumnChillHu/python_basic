# -*- coding: utf-8 -*-
"""
实现多线程的2种方式：
    1.threading.Thread类
    2.继承threading.Thread类

多线程安全 上锁的2种方式:
    1.Lock
    2.RLock
"""

"""实现多线程-方式1：threading.Thread类"""
from threading import Thread
import time


def threading_run(n):
    print("start threading task：{}".format(n))
    time.sleep(2)
    print("end threading task：{}".format(n))


def new_threading():
    threading_list = []
    for i in range(5):
        # 初始化线程：Thread(target=func_name, args=(i,))
        # target：绑定启动线程时需要执行的方法，相当于绑定run()方法。
        # args：以元组形式传递target的参数。
        threading_list.append(Thread(target=threading_run, args=(i,)))
        # 启动线程
        threading_list[i].start()


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


"""线程安全-上锁-方式1：Lock"""
from threading import Lock

num_lock = 0
# 全局锁
mutex_lock = Lock()


class MyLockThread(Thread):
    def run(self):
        global num_lock
        time.sleep(1)
        if mutex_lock.acquire():
            num_lock += 1
            time.sleep(0.5)
            num_lock += 1
            msg = self.name + ': num value is ' + str(num_lock)
            print(msg)
            mutex_lock.release()


# if __name__ == '__main__':
#     for i in range(5):
#         MyThread().start()

# RLock
# 递归锁RLock内部维护着一个Lock和一个counter，counter
# 记录acquire的次数。资源可以被多次
# require，只有线程所有的
# acquire
# 都被
# release，其他的线程才能获得资源。

# from threading import RLock
#
# num = 0
# mutex = RLock()

# class MyThread(Thread):
#     def run(self):
#         global num
#         if mutex.acquire():
#             print("thread " + self.name + " get mutex")
#             num += 1
#             time.sleep(0.5)
#             num += 1
#             print("thread " + self.name + " get num " + str(num))
#             mutex.acquire()
#             mutex.release()
#             mutex.release()


# if __name__ == '__main__':
#     for i in range(5):
#         MyThread().start()

def return_test():
    print("hi")

if __name__ == "__main__":
    # 实现多线程-方式1：threading.Thread类
    # new_threading()
    # 实现多线程-方式2：继承threading.Thread类
    new_mythreading()
    x=return_test()
    print(x)
