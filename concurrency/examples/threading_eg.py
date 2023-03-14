# -*- coding: utf-8 -*-

# todo: -多线程与单线程提效对比：1.斐波那契数列 2.阶乘与累加函数
"""
-生产-消费者
"""
import queue
import time
from threading import Thread

"""生产-消费者"""


def producer(q, data):
    q.put(data)


def consumer(q):
    while True:
        item = q.get()
        print("consumer {}".format(item))
        if item == -1:
            break


def producer_consumer():
    q = queue.Queue()
    datas = [i for i in range(500)]
    for data in datas:
        Thread(target=producer, args=(q, data)).start()
    Thread(target=consumer, args=(q,)).start()
    # 结束标志
    Thread(target=producer, args=(q, -1)).start()
    #
    q.join()


if __name__ == "__main__":
    # 生产-消费者
    producer_consumer()
