# -*- coding: utf-8 -*-
import threading
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
