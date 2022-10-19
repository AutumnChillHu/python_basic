# -*- coding: utf-8 -*-
"""
栈和队列的实现各自都可以通过deque、list、链表三种方式。
deque模块科普：https://janineee.atlassian.net/wiki/spaces/JW/pages/67633157#%E9%A1%BA%E5%BA%8F%E8%A1%A8%EF%BC%9Aqueue-%26-stack
"""

from collections import deque
from linkedlist_mo import Node


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

    def push_by_deque(self, *elements):
        """
        *elements表示接收任意个参数。
        实际参数如果是空、单个、多个：会打包成一个元组形式传入。
        实际参数是个列表，会将整个列表当做一个参数传入。"""

        # # 右端添加-右端删除
        # self.stack_by_deque.extend(elements)
        # return self.stack_by_deque

        # 左端添加-左端删除
        self.stack_by_deque.extendleft(elements)
        return self.stack_by_deque

    def pop_by_deque(self):
        # # 右端添加-右端删除
        # # 空栈会抛出异常
        # return self.stack_by_deque.pop()

        # 左端添加-左端删除
        # 空栈会抛出异常
        return self.stack_by_deque.popleft()

    def popall_by_deque(self):
        elements = []

        # # 右端添加-右端删除
        # while self.stack_by_deque:
        #     # 空栈会抛出异常
        #     elements.append(self.stack_by_deque.pop())
        # return tuple(elements)

        # 左端添加-左端删除
        while self.stack_by_deque:
            # 空栈会抛出异常
            elements.append(self.stack_by_deque.popleft())
        return tuple(elements)

    def push_by_list(self, *elements):
        """
        *elements表示接收任意个参数。
        实际参数如果是空、单个、多个：会打包成一个元组形式传入。
        实际参数是个列表，会将整个列表当做一个参数传入。"""

        self.stack_by_list.extend(elements)
        return self.stack_by_list

    def pop_by_list(self):
        return self.stack_by_list.pop()

    def popall_by_list(self):
        elements = []

        while self.stack_by_list:
            # 空栈会抛出异常
            elements.append(self.stack_by_list.pop())
        return tuple(elements)

    def push_by_linkedlist(self, node):
        """仅支持单个元素入栈"""

        if self.stack_by_linkedlist:
            node.next = self.stack_by_linkedlist
        self.stack_by_linkedlist = node
        return self.stack_by_linkedlist

    def pop_by_linkedlist(self):
        if not self.stack_by_linkedlist:
            raise IndexError("empty stack")

        node = self.stack_by_linkedlist
        self.stack_by_linkedlist = node.next
        return node

    def popall_by_linkedlist(self):
        nodes = []
        while self.stack_by_linkedlist:
            nodes.append(self.stack_by_linkedlist)
            self.stack_by_linkedlist = self.stack_by_linkedlist.next
        return tuple(nodes)


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

    def enque_by_deque(self, *elements):
        self.queue_by_deque.extend(elements)
        return self.queue_by_deque

    def deque_by_deque(self):
        return self.queue_by_deque.popleft()

    def dequeall_by_deque(self):
        elements = []
        while self.queue_by_deque:
            elements.append(self.queue_by_deque.popleft())
        return tuple(elements)

    def enque_by_list(self, *elements):
        self.queue_by_list.extend(elements)
        return self.queue_by_list

    def deque_by_list(self):
        return self.queue_by_list.pop(0)

    def dequeall_by_list(self):
        elements = []
        while self.queue_by_list:
            elements.append(self.queue_by_list.pop(0))
        return tuple(elements)

    def enque_by_linkedlist(self, node):
        """仅支持单个元素入队"""
        if not node:
            raise KeyError("empty node")

        if not self.queue_by_linkedlist_head:
            self.queue_by_linkedlist_head = node
        else:
            self.queue_by_linkedlist_end.next = node
        self.queue_by_linkedlist_end = node
        return self.queue_by_linkedlist_head

    def deque_by_linkedlist(self):
        if not self.queue_by_linkedlist_head:
            raise IndexError("empty queue")

        node = self.queue_by_linkedlist_head
        self.queue_by_linkedlist_head = self.queue_by_linkedlist_head.next
        return node

    def dequeall_by_linkedlist(self):
        elements = []
        while self.queue_by_linkedlist_head:
            elements.append(self.queue_by_linkedlist_head)
            self.queue_by_linkedlist_head = self.queue_by_linkedlist_head.next
        return tuple(elements)


if __name__ == "__main__":
    s = StackMo()
    # s.push_by_deque(1, 2, 3, None, [], (), {}, set(), 10, True, "hello", [1, "2", 3], (1, "2", 3), {1, "2", 3})
    # s.push_by_deque([1, 2, 3])
    # print(s.popall_by_deque())

    # s.push_by_list(1, 2, 3, None, [], (), {}, set(), 10, True, "hello", [1, "2", 3], (1, "2", 3), {1, "2", 3})
    # s.push_by_list([1, 2, 3])
    # print(s.popall_by_list())

    # s.push_by_linkedlist(Node(value=None))
    # s.push_by_linkedlist(Node(value=1))
    # s.push_by_linkedlist(Node(value=2))
    # s.push_by_linkedlist(Node(value=[]))
    # s.push_by_linkedlist(Node(value=()))
    # s.push_by_linkedlist(Node(value={}))
    # s.push_by_linkedlist(Node(value=set()))
    # s.push_by_linkedlist(Node(value=True))
    # s.push_by_linkedlist(Node(value="hello"))
    # s.push_by_linkedlist(Node(value=[1, "2", 3]))
    # s.push_by_linkedlist(Node(value=(1, "2", 3)))
    # s.push_by_linkedlist(Node(value={1, "2", 3}))
    # print(s.pop_by_linkedlist())
    # s.pop_by_linkedlist()
    # print("hello")

    q = QueueMo()
    q.enque_by_linkedlist(None)
