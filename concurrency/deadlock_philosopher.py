# -*- coding: utf-8 -*-
import threading
import time
from contextlib import contextmanager

"""deadlock"""


def deadlock_eat(left_stick, right_stick):
    while True:  # 因为哲学家吃一会儿、想一会儿、再吃一会儿，所以while True
        print("{} applying".format(threading.current_thread().name))
        with left_stick:
            with right_stick:
                print("{} eating".format(threading.current_thread().name))
                time.sleep(3)
        # 吃完了，思考一会儿
        print("{} thinking".format(threading.current_thread().name))
        time.sleep(6)


"""解决deadlock"""


# _local = threading.local()


def philosopher():
    people = 5
    # 一支筷子一把锁
    chopsticks_locks = [threading.Lock() for i in range(people)]
    for i in range(people):
        # 死锁
        # threading.Thread(target=deadlock_eat, args=(chopsticks_locks[i], chopsticks_locks[(i + 1) % people])).start()
        # 有序拿锁
        first_stick = chopsticks_locks[i] if i < (i + 1) % people else chopsticks_locks[(i + 1) % people]
        second_stick = chopsticks_locks[i] if i > (i + 1) % people else chopsticks_locks[(i + 1) % people]
        threading.Thread(target=eat, args=(first_stick, second_stick)).start()


def eat(first_stick, second_stick):
    while True:  # 因为哲学家吃一会儿、想一会儿、再吃一会儿，所以while True
        print("{} applying".format(threading.current_thread().name))
        first_stick.acquire()
        second_stick.acquire()

        print("{} eating".format(threading.current_thread().name))
        time.sleep(3)

        second_stick.release()
        first_stick.release()

        # 吃完了，思考一会儿
        print("{} thinking".format(threading.current_thread().name))
        time.sleep(6)


if __name__ == "__main__":
    philosopher()
