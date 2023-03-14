# -*- coding: utf-8 -*-

"""
利用生成器原始实现：yield+send

# -*- coding:utf8 -*-
def consumer():
    res = ''
    while True:
        n = yield res
        print('[CONSUMER]Consuming %s...' % n)
        res = "200 OK" if n else "500 EMPTY"

def producer(consumer):
    consumer.send(None)
    n = 0
    while n < 10:
        n = n + 1
        print('[PRODUCER]Producing %s...' % n)
        r = consumer.send(n)
        print('[PRODUCER]Consumer return: %s' % r)
    r = consumer.send(None)
    print('[PRODUCER]Consumer return: %s' % r)
    consumer.close()

if __name__ == '__main__':
    consumer = consumer()
    producer(consumer)

语法糖：async def（since Python 3.8）

from datetime import datetime
import asyncio

RESOURCE_NUM = 10000


async def do(param=0):
    print(param)
    await asyncio.sleep(1)


if __name__ == "__main__":
    start = datetime.now()
    loop = asyncio.get_event_loop()
    tasks = [do(i) for i in range(RESOURCE_NUM)]
    loop.run_until_complete(asyncio.wait(tasks))
    end = datetime.now()
    print(end - start)

gevent

import time

from gevent import monkey;

monkey.patch_socket()
import gevent
from datetime import datetime

RESOURCE_NUM = 10000

def do(param=""):
    print(param)
    gevent.sleep(1)

if __name__ == "__main__":
    start = datetime.now()
    tasks = [gevent.spawn(do, i) for i in range(RESOURCE_NUM)]
    gevent.joinall(tasks)
    end = datetime.now()
    print(end - start)
"""

if __name__ == "__main__":
    pass
