# -*- coding: utf-8 -*-
"""
-实现多进程：
    1. 使用 multiprocessing.Process类 创建进程。
    2. 使用 继承multiprocessing.Process类 的自定义类 创建进程。
    3. 使用 进程池multiprocessing.Pool类 创建进程。

-进程间通信IPC：
    1.【推荐使用】multiprocessing.Queue类：队列，进程安全。
    2.【可以使用】multiprocessing.Pipe类：管道，进程不安全。
    3.【避免使用】multiprocessing.Value/Array：共享内存，进程安全。
    4.【避免使用】multiprocessing.Manager：服务进程管理共享状态。
"""

import os
import time


def run(num):
    print("进程{} 开始run>>> pid={}, ppid={}".format(num, os.getpid(), os.getppid()))
    time.sleep(4)
    print("进程{} 结束run>>> pid={}, ppid={}".format(num, os.getpid(), os.getppid()))
    return os.getpid()


"""实现多进程-1. 使用 multiprocessing.Process类 创建进程。"""
from multiprocessing import Process

def new_multiprocess():
    for i in range(50):
        # Process(target=func_name, args=(i,))：初始化一个进程
        #   -target：绑定启动进程时需要执行的run()方法。
        #   -args：传递target绑定的方法的参数，用元组形式。
        p = Process(target=run, args=(i,))

        # start()：异步启动进程，触发run()方法的执行。
        p.start()

        # 下方介绍几种进程结束方法
        if i == 1:
            # join([time])：在当前位置阻塞主进程，直至子进程执行完毕。
            #   -time：最长阻塞时间。
            p.join()
        if i == 2:
            # terminate()：立即中断子进程，run()中的后续语句以及finally语句都不会执行。
            p.terminate()
        if i == 3:
            # kill()：与terminate()相同。只是kill()在Unix上使用SIGKILL信号实现，terminate()在Unix上使用SIGTERM信号实现。
            p.kill()

        # 下方介绍几种进程常用方法
        if i == 4:
            # is_alive()：返回True/False进程是否仍在运行
            print(p.is_alive())


"""实现多进程-2. 使用 继承multiprocessing.Process类 的自定义类 创建进程。"""
class MyMultiProcess(Process):

    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        """重写run()"""
        print("进程{} 开始run>>> pid={}, ppid={}".format(self.num, os.getpid(), os.getppid()))
        time.sleep(4)
        print("进程{} 结束run>>> pid={}, ppid={}".format(self.num, os.getpid(), os.getppid()))
        return os.getpid()


"""实现多进程-3. 使用 进程池multiprocessing.Pool类 创建进程。"""
from multiprocessing import Pool

def new_multiprocesspool():
    """方式1：显示调用pool.close()+pool.join()，释放pool资源。"""

    # Pool(num)：初始化进程池，num指定池内进程数容量。默认为os.cpu_count()，本机为8。
    pool = Pool(5)

    # 通过列表推导式起10个进程。
    #  -pool.apply(fun, args=(i,))：【别用】同步启动一个进程，相当于单进程。
    #  -pool.apply_async(fun, args=(i,))：启动一个进程。遇到进程池已满的情况，则会等到池中有进程结束，让出空位。
    results = [pool.apply_async(run, (i,)) for i in range(10)]
    # pool.apply_async()返回ApplyResult对象，通过get()方法获取进程run()的返回结果。get()会阻塞当前进程。
    print([res.get() for res in results])

    # 结束&释放进程池
    #  -pool.terminate()：进程池停止接收新任务，立即中断子进程的执行，进程池立即关闭。
    #  -pool.close()：进程池停止接收新任务，当所有子进程执行完毕后，进程池才会关闭。此方法不会阻塞主进程。
    #  -pool.join()：阻塞主进程，直至进程池关闭。必须在close或terminate()之后使用。
    # 推荐套招close()+join()：解决因单独使用close()/terminate()导致主进程已经结束，但是子进程还未结束的问题。
    pool.close()
    pool.join()


def new_multiprocesspool_endby_with():
    """方式2：使用with管理pool资源的启动和释放"""
    with Pool(10) as pool:
        results = [pool.apply_async(run, (i,)) for i in range(10)]
        print([res.get() for res in results])


"""进程间通信IPC-multiprocessing.Queue类"""
from multiprocessing import Queue

def iPC_by_queue():
    q = Queue()

    # 写进程
    p_write = Process(target=write_queue, args=(q, [1, 2, 3, True, "hello", "world", "END", 999, 998]))
    p_write.start()

    # 读进程：主进程
    while True:
        # queue.get([,block] [,timeout])：获取并删除一个元素。FIFO。
        #   -block：队列空时，是否阻塞等待至有元素。默认为True。若为False，不阻塞，抛出Queue.Empty异常。
        #   -timeout：阻塞模式中，指定最大等待时间。超时后仍没有新增项，抛出Queue.Empty异常。
        item = q.get()
        print("读进程{}读取数据：{}，父进程{}".format(os.getpid(), item, os.getppid()))

        # 约定结束规则。
        if item == "END":
            break

    p_write.join()

    # 下方介绍几种queue常用方法
    print("empty queue? {}".format(q.empty()))
    print("full queue? {}".format(q.full()))


def write_queue(q, value_list):
    for v in value_list:
        print("写进程{}写入数据：{}，父进程{}".format(os.getpid(), v, os.getppid()))
        # queue.put(item [,block] [,timeout] )：添加item。
        #   -block：队列满时，是否阻塞等待直至有空位。默认为True。若为False，不阻塞，抛出Queue.Full异常。
        #   -timeout：阻塞模式中，指定最大等待时间。超时将抛出Queue.Full异常。
        q.put(v)


"""进程间通信IPC-multiprocessing.Pipe"""
from multiprocessing import Pipe

def iPC_by_pipe():
    # Pipe(): 初始化，返回两个连接对象，代表管道的两端。
    #   -每个连接对象都有send()和recv()，双端都允许写入和读取，即默认是双工的。
    #   -left写入的，只有right能读；right写入的，只有left能读。
    left_conn, right_conn = Pipe()
    # 写进程
    process_write = Process(target=write_pipe, args=(left_conn, [1, 2, 3, True, "hello", "world", "END", 999, 998]))
    process_write.start()

    # 读进程：主进程
    while True:
        item = right_conn.recv()
        print("读进程{}读取数据：{}，父进程{}".format(os.getpid(), item, os.getppid()))

        # 约定结束规则。
        if item == "END":
            break

    process_write.join()

def write_pipe(conn, value_list):
    for v in value_list:
        print("写进程{}写入数据：{}，父进程{}".format(os.getpid(), v, os.getppid()))
        conn.send(v)


"""进程间通信IPC-multiprocessing.Value/Array"""
from multiprocessing import Value, Array

def iPC_by_value_and_array():
    double = Value('d', 1.23)  # double
    int = Value('i', 1)  # int
    char = Value('u', "a")  # unicode字符, one character
    arr_int = Array('i', range(10))
    arr_char = Array('u', ['a', 'b', 'c', 'd', 'e'])

    p = Process(target=run_ipc_by_value_and_array, args=(double, int, char, arr_int, arr_char))
    p.start()
    p.join()
    print(double.value, int.value, char.value, arr_int[:], arr_char[:])


def run_ipc_by_value_and_array(double, int, char, arr_int, arr_char):
    double.value += 1
    int.value += 1
    char.value = "z"
    # arr_int.value.append(999)
    arr_char[0] = "z"


"""进程间通信IPC-multiprocessing.Manager"""
from multiprocessing import Manager


def iPC_by_manager():
    with Manager() as manager:
        dic = manager.dict()
        li = manager.list([1, 2, "a", "xyz"])
        double = manager.Value('d', 1.23)
        int = manager.Value('i', 1)
        char = manager.Value('u', "a")

        p = Process(target=run_ipc_by_manager, args=(dic, li, double, int, char))
        p.start()
        p.join()

        print(dic, li, double.value, int.value, char.value)


def run_ipc_by_manager(dic, li, double, int, char):
    dic[1] = os.getpid()
    li.append(os.getpid())
    li[0] += 100
    double.value += 1
    int.value += 1
    char.value = 'z'


if __name__ == '__main__':
    # 实现多进程
    # new_multiprocess()
    new_multiprocesspool()
    # new_multiprocesspool_endby_with()

    # 进程间通信IPC
    # iPC_by_queue()
    # iPC_by_pipe()
    # iPC_by_value_and_array()
    # iPC_by_manager()
    pass
