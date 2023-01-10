# -*- coding: utf-8 -*-
"""
实现多线程的2种方式
1.threading.Thread
2.继承threading.Thread类：重写run方法
"""

"""实现多线程方式1：threading.Thread类"""
from threading import Thread
import time


def fun(n):
    print("start task：{}".format(n))
    time.sleep(2)
    print("end task：{}".format(n))


def new_threding():
    thread_list = []
    for i in range(5):
        thread_list.append(Thread(target=fun, args=(i,)))
        thread_list[i].start()


"""实现多线程方式2：继承threading.Thread类，重写run方法"""


class MyThread(Thread):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def run(self):
        print("线程开始：{}".format(self.msg))
        time.sleep(3)
        print("线程终止：{}".format(self.msg))


def new_mythreading():
    thread_list = []
    for i in range(5):
        thread_list.append(MyThread(i))
        thread_list[i].start()

"""线程安全："""

Lock

from threading import Thread, Lock
import time

num = 0
mutex = Lock()  # 全局锁

class MyThread(Thread):
  def run(self):
    global num
    time.sleep(1)
    if mutex.acquire():
      num += 1
      time.sleep(0.5)
      num += 1
      msg = self.name + ': num value is ' + str(num)
      print(msg)
      mutex.release()

if __name__ == '__main__':
  for i in range(5):
    MyThread().start()

RLock 递归锁RLock内部维护着一个Lock和一个counter，counter 记录acquire的次数。资源可以被多次 require，只有线程所有的 acquire 都被 release，其他的线程才能获得资源。

from threading import Thread, RLock
import time

num = 0
mutex = RLock()

class MyThread(Thread):
  def run(self):
    global num
    if mutex.acquire():
      print("thread " + self.name + " get mutex")
      num += 1
      time.sleep(0.5)
      num += 1
      print("thread " + self.name + " get num " + str(num))
      mutex.acquire()
      mutex.release()
      mutex.release()
if __name__ == '__main__':
  for i in range(5):
    MyThread().start()

if __name__ == "__main__":
    pass
