# -*- coding: utf-8 -*-

"""
实现多进程的三种方式：
1. multiprocessing.Process类
2. 继承multiprocessing.Process类
3. 进程池multiprocessing.Pool类
"""

import os
import time

"""方式1：multiprocessing.Process类"""
from multiprocessing import Process


def process_run(num):
    # 打印当前进程id
    print("process_run 进程开始{}>>> pid={}".format(num, os.getpid()))
    time.sleep(5)
    print("process_run 进程结束{}>>> pid={}".format(num, os.getpid()))
    return None


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

    # 终止子进程：发出终止信号，返回。子进程执行被打断，异步结束。
    # 执行过程被打断 & 异步调用。
    # 所以processes[0]不会有进程结束那条打印语句
    processes[0].terminate()
    # 判断子进程是否存活
    print(processes[0].is_alive())

    # 终止子进程：发出终止信号，并且等待直到子进程执行结束后，在返回。
    # 执行完毕 & 同步调用。
    # 所以processes[1]会有进程结束那条打印语句
    processes[1].join()
    print(processes[1].is_alive())

    print(processes[0].is_alive())
    print(processes[1].is_alive())


"""方式2：继承multiprocessing.Process类"""


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


"""方式3：进程池multiprocessing.Pool模块"""
from multiprocessing import Pool


def processpool_run(num):
    print("进程开始>>> num={}, pid={}".format(num, os.getpid()))
    time.sleep(3)
    print("进程结束>>> num={}, pid={}".format(num, os.getpid()))
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


if __name__ == '__main__':
    # 方式1：multiprocessing.Process类
    # new_multiprocess()
    # 方式2：继承multiprocessing.Process类
    # new_mymultiprocess()
    # 方式3：multiprocessing.Pool类，异步。
    # async_multiprocesspool()
    # 方式3：multiprocessing.Pool类，同步。
    sync_multiprocesspool()
