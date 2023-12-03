# -*- coding: utf-8 -*-

from collections import deque
from linkedlistMO import Node


class StackMo():

    def __init__(self):
        """
        1.stack_by_deque: 在同一端进行入栈、出栈。
        2.stack_by_list: 在队尾进行入栈、出栈。
        3.self.stack_by_linkedlist: 在链表头部进行出栈、入栈
        """
        self.stack_by_deque = deque()
        self.stack_by_list = []
        self.stack_by_linkedlist = None

    def push_list(self, element):
        """
        *elements表示接收任意个参数。
        实际参数如果是空、单个、多个：会打包成一个元组形式传入。
        实际参数是个列表，会将整个列表当做一个参数传入。"""

        self.stack_by_list.append(element)
        return self.stack_by_list

    def pop_list(self):
        return self.stack_by_list.pop()

    def push_linkedlist(self, node):
        if self.stack_by_linkedlist:
            node.next = self.stack_by_linkedlist
        self.stack_by_linkedlist = node

        return self.stack_by_linkedlist

    def pop_linkedlist(self):
        if not self.stack_by_linkedlist:
            return None

        node = self.stack_by_linkedlist
        self.stack_by_linkedlist = node.next
        return node

    def push_deque(self, element):
        # # 右端添加-右端删除
        # self.stack_by_deque.append(elements)
        # return self.stack_by_deque

        # 左端添加-左端删除
        self.stack_by_deque.appendleft(element)
        return self.stack_by_deque

    def pop_deque(self):
        # # 右端添加-右端删除
        # # 空栈会抛出异常
        # return self.stack_by_deque.pop()

        # 左端添加-左端删除
        # 空栈会抛出异常
        return self.stack_by_deque.popleft()


class QueueMo():
    def __init__(self):
        """
        1.queue_by_deque: 在不同端进行入队、出队。（只示例一种实现）
        2.queue_by_list: 在不同端进行入队、出队。（只示例一种实现）
        3.queue_by_linkedlist: 在链表尾部入队，链表头部出队。
        """
        self.queue_by_deque = deque()
        self.queue_by_list = []
        self.queue_by_linkedlist_head = None
        self.queue_by_linkedlist_end = None

    def enque_list(self, element):
        self.queue_by_list.append(element)
        return self.queue_by_list

    def deque_list(self):
        return self.queue_by_list.pop(0)

    def enque_linkedlist(self, node):
        """尾部入队"""
        if not node:
            raise KeyError("empty node")

        if not self.queue_by_linkedlist_head:
            self.queue_by_linkedlist_head = node
        else:
            self.queue_by_linkedlist_end.next = node
        self.queue_by_linkedlist_end = node
        return self.queue_by_linkedlist_head

    def deque_linkedlist(self):
        """头部出队"""
        if not self.queue_by_linkedlist_head:
            raise IndexError("empty queue")

        node = self.queue_by_linkedlist_head
        self.queue_by_linkedlist_head = self.queue_by_linkedlist_head.next
        return node

    def enque_by_deque(self, element):
        self.queue_by_deque.append(element)
        return self.queue_by_deque

    def deque_by_deque(self):
        return self.queue_by_deque.popleft()


if __name__ == "__main__":
    pass
