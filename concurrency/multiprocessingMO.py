# -*- coding: utf-8 -*-

"""
-实现多进程的3种方式：
    1. multiprocessing.Process类
    2. 继承multiprocessing.Process类
    3. 进程池multiprocessing.Pool类

-进程间无法通信举例

-进程间通信IPC的3种方式:
    1.multiprocessing.Queue类：共享队列，进程安全。
    2.multiprocessing.Pipe类：共享管道，进程不安全。
    3.multiprocessing.Manager：共享内存，进程安全。
      multiprocessing.Value/Array：共享内存，进程不安全。
    4.信号量：传递multiprocessing.Semaphore，同时允许一定数量的线程更改数据
"""

import os
import time

"""实现多进程-方式1：multiprocessing.Process类"""
from multiprocessing import Process


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

    # terminate()终止进程：立即中断进程，并结束。
    # 所以processes[0]没有打印语句
    processes[0].terminate()
    # join()终止进程：等待进执行完毕后，再结束。
    # 所以processes[1]会有打印语句
    processes[1].join()

    # 判断进程是否存活
    print(processes[0].is_alive())
    print(processes[1].is_alive())
    print(processes[4].is_alive())

    time.sleep(10)
    print(processes[4].is_alive())


def process_run(num):
    # 打印当前进程id
    print("进程开始run{}>>> pid={}, ppid={}".format(num, os.getpid(), os.getppid()))
    time.sleep(4)
    print("进程结束run{}>>> pid={}, ppid={}".format(num, os.getpid(), os.getppid()))


"""实现多进程-方式2：继承multiprocessing.Process类"""


class MyMultiProcess(Process):
    def __init__(self):
        super().__init__()

    def run(self):
        print("进程开始run>>> pid={}".format(os.getpid()))
        time.sleep(5)
        print("进程结束run>>> pid={}".format(os.getpid()))


def new_mymultiprocess():
    processes = []

    for i in range(3):
        processes.append(MyMultiProcess())

    for p in processes:
        # 异步启动进程，start()触发执行run()方法。
        p.start()


"""实现多进程-方式3：进程池multiprocessing.Pool模块"""
from multiprocessing import Pool


def multiprocesspool():
    # 初始化进程池，提供池内进程数。
    pool = Pool(5)
    results = []
    for i in range(20):
        # 异步启动多进程。
        # 遇到进程池已满的情况，则会等待直至池中有进程结束，让出空位。
        result = pool.apply_async(processpool_run, args=(i,))
        # pool.apply(fun, args=(i,))：同步启动多进程，相当于单进程，别用。
        results.append(result)

    # pool.terminate()：中止并关闭pool。停止接受新进程，立即中断进程，并结束。
    # pool.close()：    关闭pool。停止接收新任务，等待进程执行完毕后结束。等待过程并不影响主进程的继续执行。
    # pool.join()：     阻塞主进程，等待所有子进程执行完毕。必须在close或terminate()之后使用。
    # 单独使用close()或terminate()方法，可能会导致：主进程已经结束，但是子进程还未结束的情况。
    # 与join()方法组合使用，可以避免此问题。
    pool.close()
    pool.join()

    for i in range(len(results)):
        # results[i]为ApplyResult对象，通过get方法获取进程执行结果。
        results[i] = results[i].get()
    return results


def processpool_run(num):
    print("进程开始run>>> num={}, pid={}, ppid={}".format(num, os.getpid(), os.getppid()))
    time.sleep(3)
    print("进程结束run>>> num={}, pid={}, ppid={}".format(num, os.getpid(), os.getppid()))
    return num


"""进程间无法通信举例"""
GLOBAL_VAR = ["a", "b", [1, 2]]


def father_process():
    li = ["a", "b", [1, 2]]
    s = "hello"
    p1 = Process(target=p_run, args=(li, s))
    p2 = Process(target=p_run, args=(li, s))
    print("li:{}, s:{}, GLOBAL_VAR:{}".format(li, s, GLOBAL_VAR))


def p_run(li, s):
    #
    li.append(os.getpid())
    li[2].append(os.getpid())
    s += os.getpid()
    # 父进程相同的
    GLOBAL_VAR.append(str(os.getpid()))
    GLOBAL_VAR.append(str(os.getpid()))


"""进程间通信-方式1：multiprocessing.Queue类
1. 队列 FIFO，一端可读，一端可写。
2. 进程安全：底层队列使用管道和锁定实现。
"""
from multiprocessing import Queue


def write_queue(q, value_list):
    for v in value_list:
        print("写进程{}写入数据：{}，父进程{}".format(os.getpid(), v, os.getppid()))
        # queue.put(item [,block] [,timeout] )：添加item。
        #   -block：队列满时，是否阻塞等待至有空位。默认为True。若为False，不阻塞，抛出Queue.Full异常。
        #   -timeout：阻塞模式中，指定最大等待时间。超时将抛出Queue.Full异常。
        q.put(v)
        time.sleep(1)


def read_queue(q):
    while True:
        # queue.get([,block] [,timeout])：获取并删除元素。
        #   -block：队列空时，是否阻塞等待至有元素。默认为True。若为False，不阻塞，抛出Queue.Empty异常。
        #   -timeout：阻塞模式中，指定最大等待时间。超时后仍没有新增项，抛出Queue.Empty异常。
        item = q.get()
        print("读进程{}读取数据：{}，父进程{}".format(os.getpid(), item, os.getppid()))

        # 约定结束规则。
        if item == "END":
            break


def iPC_by_queue():
    q = Queue()

    p_write = Process(target=write_queue, args=(q, [1, 2, 3, True, "hello", "world", "END", 999]))
    p_read = Process(target=read_queue, args=(q,))

    # 异步启动进程
    p_write.start()
    # p_read.start()

    # 终止进程
    p_write.join()
    # p_read.join()

    while True:
        # queue.get([,block] [,timeout])：获取并删除元素。
        #   -block：队列空时，是否阻塞等待至有元素。默认为True。若为False，不阻塞，抛出Queue.Empty异常。
        #   -timeout：阻塞模式中，指定最大等待时间。超时后仍没有新增项，抛出Queue.Empty异常。
        item = q.get()
        print("读进程{}读取数据：{}，父进程{}".format(os.getpid(), item, os.getppid()))

        # 约定结束规则。
        if item is True:
            break

    p_read.start()
    p_read.join()


"""进程间通信-方式2：multiprocessing.Pipe
1. 管道 FIFO，默认双工向，返回两个连接对象，代表管道的两端。
2. 每个连接对象都有send()和recv()，双端都允许写入和读取。
   left写入的，只有right能读；
   right写入的，只有left能读。
3. 进程不安全。
"""
from multiprocessing import Pipe


def write_pipe(p, value_list):
    for v in value_list:
        print("写进程{}写入数据：{}，父进程{}".format(os.getpid(), v, os.getppid()))
        p.send(v)
        time.sleep(1)


def read_pipe(p):
    while True:
        item = p.recv()
        print("读进程{}读取数据：{}，父进程{}".format(os.getpid(), item, os.getppid()))


def iPC_by_pipe():
    p_left, p_right = Pipe()
    process_write1 = Process(target=write_pipe, args=(p_left, [1, 2, 3]))
    process_write2 = Process(target=write_pipe, args=(p_right, ["a", "b", "c"]))
    process_read1 = Process(target=read_pipe, args=(p_left,))
    process_read2 = Process(target=read_pipe, args=(p_right,))

    process_write1.start()
    process_write2.start()
    process_read1.start()
    process_read2.start()

    process_write1.join()
    process_write2.join()
    process_read1.join()
    process_read2.join()


"""进程间通信-方式3：multiprocessing.Manager
1. Manager进程安全。
"""

"""Value/Array/
1. multiprocessing.Manager：共享内存，进程安全。
      multiprocessing.Value/Array：共享内存，进程不安全，需要加锁。
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


# if __name__ == '__main__':
#     manager = Manager()
#     ma_dic = manager.dict()  # manager中的字典结构
#     ma_li = manager.list()  # manager中的列表结构
#     dic = {}  # 普通字典
#     li = []  # 普通列表
#
#     processes = []
#     for i in range(5):
#         processes.append(Process(target=func, args=(ma_dic, dic, ma_li, li)))
#         processes[i].start()
#     for p in processes:
#         p.join()
#
#     print("manager.dict：", ma_dic)
#     print("dict：", dic)
#     print("manager.list：", ma_li)
#     print("list：", li)
# // 输出
# manager.dict： {74427: 74427, 74429: 74429, 74430: 74430, 74428: 74428, 74426: 74426}
# dict： {}
# manager.list： [74427, 74429, 74430, 74428, 74426]
# list： []

if __name__ == '__main__':
    # new_multiprocess()
    # new_mymultiprocess()
    # multiprocesspool()

    iPC_by_queue()
    # iPC_by_pipe()
    pass
