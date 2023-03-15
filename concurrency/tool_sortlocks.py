# -*- coding: utf-8 -*-
import threading
import time
from contextlib import contextmanager

_local = threading.local()


@contextmanager
def acquire(*locks):
    # 按照id顺序进行排列(默认升序)
    locks = sorted(locks, key=lambda x: id(x))

    # 检查确保locks没有出现乱序
    acquired = getattr(_local, "acquired", [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    _local.acquired = acquired.extend(locks)

    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # 逆序释放锁。先释放最内层的锁。
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


def philosopher():
    people = 5
    # 一支筷子一把锁
    chopsticks_locks = [threading.Lock() for i in range(people)]
    for i in range(people):
        # 死锁
        # threading.Thread(target=deadlock_eat, args=(chopsticks_locks[i], chopsticks_locks[(i + 1) % people])).start()
        # 有序拿锁，不会死锁
        threading.Thread(target=right_eat, args=(chopsticks_locks[i], chopsticks_locks[(i + 1) % people])).start()


def right_eat(left_stick, right_stick):
    while True:
        print("{} applying".format(threading.current_thread().name))
        with acquire(left_stick, right_stick):
            print("{} eating".format(threading.current_thread().name))
            time.sleep(3)


def deadlock_eat(left_stick, right_stick):
    while True:
        print("{} applying".format(threading.current_thread().name))
        with left_stick:
            with right_stick:
                print("{} eating".format(threading.current_thread().name))
                time.sleep(3)


if __name__ == "__main__":
    philosopher()
