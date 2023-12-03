# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def new_linkedlist(vals):
    """新建链表"""

    if not vals:
        return None

    head = Node(value=vals[0])
    p = head
    for i in range(1, len(vals)):
        p.next = Node(value=vals[i])
        p = p.next
    return head


def linkedlist_tolist(head):
    """链表转换为list"""

    li = []
    p = head

    while p:
        li.append(p.value)
        p = p.next
    return li


if __name__ == "__main__":
    nodes = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    head = new_linkedlist(nodes)
    print(linkedlist_tolist(head))
