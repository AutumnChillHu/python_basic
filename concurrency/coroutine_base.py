# -*- coding: utf-8 -*-
"""
-实现协程
    1. yield 生成器原始实现
    2. async+await 语法糖
"""

"""实现协程-1. yield 生成器原始实现"""
def new_coroutine_by_yield():
    con = consumer()
    con.send(None)
    # 生产者
    for i in range(10):
        con.send(i)
    con.close()

def consumer():
    print("start consumer")
    try:
        while True:
            data = yield -1
            print("consuming {} from producer".format(data))
    except GeneratorExit:
        print("consumer closed")


"""实现协程-2. async+await 语法糖"""
import asyncio

def new_coroutine_by_asyncawait():
    loop = asyncio.get_event_loop()
    tasks = [task(i) for i in range(100)]
    loop.run_until_complete(asyncio.wait(tasks))


# 协程函数：定义形式为 async def 的函数。
async def task(param):
    print(param)
    await asyncio.sleep(1)


if __name__ == "__main__":
    # 实现协程
    # new_coroutines_by_yield()
    # new_coroutines_by_asyncawait()
    pass
