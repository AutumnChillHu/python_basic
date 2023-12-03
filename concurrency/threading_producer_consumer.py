# -*- coding: utf-8 -*-
"""多线程实现生产-消费者"""
import queue
from threading import Thread

def producer_consumer():
    # 队列 FIFO
    q = queue.Queue()
    data = [i for i in range(500)]
    data.append(-1)  # 结束生产标志

    # 多线程生产
    for i in data:
        Thread(target=producer, args=(q, i)).start()
    # 消费者
    th = Thread(target=consumer, args=(q,))
    th.start()
    # 消费完
    th.join()

def producer(q, data):
    """生产者"""
    q.put(data)

def consumer(q):
    """消费者"""
    while True:
        item = q.get()
        print("consumer {}".format(item))
        if item == -1:
            break

if __name__ == "__main__":
    producer_consumer()
