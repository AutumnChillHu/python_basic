# -*- coding: utf-8 -*-

"""
实现多进程的3种方式：
    1. multiprocessing.Process类
    2. 继承multiprocessing.Process类
    3. 进程池multiprocessing.Pool类

进程间通信的3种方式:
    1.multiprocessing.Queue类：共享数据队列，进程安全。
    2.multiprocessing.Pipe类：共享数据管道，进程不安全需要加锁。
    3.multiprocessing.Value/Array/Manager：共享内存，进程不安全需要加锁。
    4.信号量：传递multiprocessing.Semaphore，同时允许一定数量的线程更改数据
"""

import os
import time

"""实现多进程-方式1：multiprocessing.Process类"""
from multiprocessing import Process


def process_run(num):
    # 打印当前进程id
    print("process_run 进程开始{}>>> pid={}".format(num, os.getpid()))
    time.sleep(5)
    print("process_run 进程结束{}>>> pid={}".format(num, os.getpid()))


def new_multiprocess():
    processes = []
    for i in range(5):
        # 初始化进程：Process(target=func_name, args=(i,))
        # target：调用对象，绑定启动进程时需要执行的方法。相当于绑定run()方法。
        # args：传递target的参数，以元组形式传递。
        processes.append(Process(target=process_run, args=(i,)))

    for p in processes:
        # 异步启动进程，start()方法触发执行target所绑定的方法。
        p.start()
    time.sleep(2)

    # terminate()终止子进程：发出终止信号，返回。子进程执行被打断，异步结束。
    # 执行过程被打断 & 异步调用。
    # 所以processes[0]不会有进程结束那条打印语句
    processes[0].terminate()
    # 判断子进程是否存活
    print(processes[0].is_alive())

    # join()终止子进程：发出终止信号，并且等待直到子进程执行结束后，在返回。
    # 执行完毕 & 同步调用。
    # 所以processes[1]会有进程结束那条打印语句
    processes[1].join()
    print(processes[1].is_alive())

    print(processes[0].is_alive())
    print(processes[1].is_alive())


"""实现多进程-方式2：继承multiprocessing.Process类"""


class MyMultiProcess(Process):
    def __init__(self):
        super().__init__()

    def run(self):
        print("run 进程开始>>> pid={}".format(os.getpid()))
        time.sleep(5)
        print("run 进程结束>>> pid={}".format(os.getpid()))


def new_mymultiprocess():
    processes = []

    for i in range(3):
        processes.append(MyMultiProcess())

    for p in processes:
        # 异步启动进程，start()触发执行执行run()方法。
        p.start()


"""实现多进程-方式3：进程池multiprocessing.Pool模块"""
from multiprocessing import Pool


def processpool_run(num):
    print("进程开始>>> num={}, pid={}, ppid={}".format(num, os.getpid(), os.getppid()))
    time.sleep(3)
    print("进程结束>>> num={}, pid={}, ppid={}".format(num, os.getpid(), os.getppid()))
    return num


def async_multiprocesspool():
    """异步启动多进程"""

    # 初始化进程池，提供指定数量的进程供调用。
    pool = Pool(5)
    results = []
    for i in range(20):
        # pool.apply_async(fun, args=(i,))：启动进程，异步执行。
        # 当有新进程请求提交到pool中时，如果进程池已满：请求会等待，直到池中有进程结束，让出池中空位。
        results.append(pool.apply_async(processpool_run, args=(i,)))

    # 异步执行不会阻塞主进程，所以可能主进程结束了，但是子进程还未结束。
    # 为了避免这种情况，通常会和close()/terminate() + join()方法一起组合使用。
    # pool.terminate()：立刻结束，停止正在处理的，也停止接受新任务。
    # pool.close()：不在接收新任务，但会等手头任务处理完毕后结束。
    # pool.join()：主进程阻塞，等待所有子进程执行完毕。必须在close或terminate()之后使用。
    pool.close()
    pool.join()

    for i in range(len(results)):
        # results[i]为ApplyResult对象，通过get方法获取结果。
        results[i] = results[i].get()
    print(results)


def sync_multiprocesspool():
    """同步启动多进程：相当于单进程，不推荐。"""
    results = []
    pool = Pool(5)
    for i in range(30):
        # pool.apply(fun, args=(i,))：启动进程，同步执行。不推荐。
        # 因为即使在进程池没有满时，有新的进程请求，也会等当前进程执行完了，才能执行下一个进程。相当于单进程顺序执行。
        results.append(pool.apply(processpool_run, args=(i,)))
    pool.close()
    pool.join()
    print(results)


"""进程间通信-方式1：multiprocessing.Queue类 共享数据队列，进程安全
1. 队列 FIFO，一端可读，一端可写。
2. 进程安全：底层队列使用管道和锁定实现。
"""
from multiprocessing import Queue


def write_queue(q, value_list):
    for v in value_list:
        print("写进程写入数据：", v)
        # queue.put(item[, block[, timeout]] )：插入数据item。
        # block：是否允许阻塞。默认为True允许阻塞。若为False，不阻塞，抛出Queue.Full异常。
        # timeout：阻塞模式中，指定最大等待时间。超时将抛出Queue.Full异常。
        q.put(v)


def read_queue(q):
    while True:
        # queue.get([block[, timeout]])：获取并删除元素。
        # block：是否允许控制阻塞，默认为True允许阻塞，直至队列中有元素。若为False，不阻塞，抛出Queue.Empty异常。
        # timeout：阻塞模式中，指定最大等待时间。超时后仍没有新增项，抛出Queue.Empty异常。
        item = q.get()
        print("读进程读取数据：", item)
        time.sleep(2)

        # 约定结束规则。
        # 无结束规则时，线程一直存活。
        if item == "END":
            break


def iPC_by_queue():
    # queue([maxsize])：初始化队列。
    # maxsize：队列中允许的最大项数     ，如果队列已满，将会发生阻塞。
    q = Queue()

    # 读、写进程
    p_write = Process(target=write_queue, args=(q, [0, 1, 2, 3, True, 4, "hello", "world", "END", 999]))
    p_read = Process(target=read_queue, args=(q,))

    # 异步启动进程
    p_write.start()
    p_read.start()

    # 终止进程
    p_write.join()
    p_read.join()


"""进程间通信-方式2：multiprocessing.Pipe
1. 管道，默认是双工向的。返回两个连接对象，代表管道的两端。
2. 每个连接对象都有send()和recv()，即双端都允许写入和读取，但其工作方式如下：
    p_left.send(item)写入数据，p_right.recv()能够读取到数据。
    同理，p_right.send(item)写入数据，p_left.recv()能够读取到数据。
3. 管道只适用于多个进程源于同一个父进程的情况。
"""
from multiprocessing import Pipe


def write_pipe(p, value_list):
    for v in value_list:
        print("写进程{}写入数据：{}，父进程{}".format(os.getpid(), v, os.getppid()))
        p.send(v)


def read_pipe(p):
    while True:
        item = p.recv()
        print("读进程{}读取数据：{}，父进程{}".format(os.getpid(), item, os.getppid()))
        time.sleep(2)


def iPC_by_pipe():
    p_left, p_right = Pipe()
    process_write1 = Process(target=write_pipe, args=(p_left, [1, 2, 3]))
    process_write2 = Process(target=write_pipe, args=(p_right, ["a", "b", "c"]))
    process_read1 = Process(target=read_pipe, args=(p_left,))
    process_read2 = Process(target=read_pipe, args=(p_right,))

    process_write1.start()
    process_write2.start()
    process_write1.join()
    process_write2.join()

    process_read1.start()
    process_read2.start()
    process_read1.join()
    process_read2.join()


"""进程间通信-方式3：multiprocessing.Value/Array/Manager
1. 
"""

# 如果多个进程不是源于同一个父进程，只能用共享内存，信号量等方式。
# 使用到线程池的时候，会涉及到主进程和父进程之间的通信，需要使用Manager。
#
# 共享原理：在内中开辟一块空间，进程可以写入内容和读取内容完成通信，但是每次写入内容会覆盖之前内容。内存共享是不安全的。不推荐。
#
# Manager：对于复杂的数据结构，Manager是一种较为高级的多进程通信方式，它能支持Python支持的任何数据结构（list
# dict
# queue
# string等等）。manager据说是加锁了的，是安全的。        原理是先启动一个ManagerServer进程，这个进程是阻塞的，它监听一个socket。                然后其他进程ManagerClient，通过socket来连接到ManagerServer，实现通信。

from multiprocessing import Manager


def func(ma_dic, dic, ma_li, li):
    ma_dic[os.getpid()] = os.getpid()
    dic[os.getpid()] = os.getpid()
    ma_li.append(os.getpid())
    li.append(os.getpid())


if __name__ == '__main__':
    manager = Manager()
    ma_dic = manager.dict()  # manager中的字典结构
    ma_li = manager.list()  # manager中的列表结构
    dic = {}  # 普通字典
    li = []  # 普通列表

    processes = []
    for i in range(5):
        processes.append(Process(target=func, args=(ma_dic, dic, ma_li, li)))
        processes[i].start()
    for p in processes:
        p.join()

    print("manager.dict：", ma_dic)
    print("dict：", dic)
    print("manager.list：", ma_li)
    print("list：", li)
# // 输出
# manager.dict： {74427: 74427, 74429: 74429, 74430: 74430, 74428: 74428, 74426: 74426}
# dict： {}
# manager.list： [74427, 74429, 74430, 74428, 74426]
# list： []

if __name__ == '__main__':
    # 实现进程方式1：multiprocessing.Process类
    # new_multiprocess()
    # 实现进程方式2：继承multiprocessing.Process类
    # new_mymultiprocess()
    # 实现进程方式3：multiprocessing.Pool类，异步。
    # async_multiprocesspool()
    # 实现进程方式3：multiprocessing.Pool类，同步。
    # sync_multiprocesspool()

    # 进程间通信方式1:multiprocessing.Queue类
    # iPC_by_queue()
    # 进程间通信方式2:multiprocessing.Pipe类
    iPC_by_pipe()
    # 进程间通信方式3:multiprocessing.Pipe类
    iPC_by_pipe()
