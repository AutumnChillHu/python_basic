# -*- coding: utf-8 -*-
"""数据结构-链表专题"""
from collections import deque

from datastructure.linkedlistMO import Node


def pop_target_node(head, value):
    """删除目标节点
    时间复杂度：O(n)
    空间复杂度：O(1)
    leetcode testcases：https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof/
    """
    if not head:
        return head
    if head.value == value:
        return head.next
    pre = head
    while pre.next:
        if pre.next.value == value:
            pre.next = pre.next.next
            return head
        pre = pre.next
    return head


def merge_two_sorted_linkedlist(head1, head2):
    """合并两个有序链表
    时间复杂度：O(m+n)
    空间复杂度：O(m+n)
    leetcode testcases：https://leetcode.cn/problems/merge-two-sorted-lists/
    """
    pre_newhead = Node()
    cur = pre_newhead
    while head1 and head2:
        if head1.value <= head2.value:
            cur.next = head1
            head1 = head1.next
        else:
            cur.next = head2
            head1 = head2.next
        cur = cur.next
    cur.next = head1 if head1 else head2
    return pre_newhead.next


def find_first_common_node(head1, head2):
    """两个链表的第一个公共节点
    时间复杂度：O(m+n)
    空间复杂度：O(m+n)
    leetcode testcases：无
    """
    if not head1 or not head2:
        return None

    # 入栈，反转链表
    stack1, stack2 = [], []
    p1, p2 = head1, head2
    while p1:
        stack1.append(p1)
        p1 = p1.next
    while p2:
        stack2.append(p2)
        p2 = p2.next

    # 从尾到头对比
    common_node = None
    while stack1 and stack2:
        ele1, ele2 = stack1.pop(), stack2.pop()
        if ele1 is not ele2:
            return common_node
        common_node = ele1
    return common_node


def reverse_linkedlist_by_iteration(head):
    """原地反转链表
    时间复杂度：O(n)
    空间复杂度：O(1)
    leetcode testcases：https://leetcode.cn/problems/reverse-linked-list/
    """
    if not head or not head.next:
        return head

    pre, curr, after = None, head, None
    while curr:
        after = curr.next  # 1）更新after
        curr.next = pre  # 2）反转方向
        pre = curr  # 3）更新pre
        curr = after  # 4）更新curr
    return pre


def reverse_linkedlist_by_recursion(node):
    """原地反转链表
    时间复杂度：O(n)
    空间复杂度：O(1)
    leetcode testcases：https://leetcode.cn/problems/reverse-linked-list/
    """
    if not node or not node.next:  # 递归终止
        return node

    newhead = reverse_linkedlist_by_recursion(node.next)
    node.next.next = node  # 箭头改方向
    node.next = None  # 保证单向
    return newhead


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head = reverse_linkedlist_by_recursion(head)
while head:
    print(head.value)
    head = head.next


def output_linkedlist_reversed_by_stack(head):
    """逆序打印链表
    时间复杂度：O(n)
    空间复杂度：O(n)
    leetcode testcases：无
    """
    if not head:
        return None

    result = deque()
    while head:
        result.appendleft(head.value)
        head = head.next
    return result


def output_linkedlist_reversed_by_recursion(node):
    """逆序打印链表
    时间复杂度：O(n)
    空间复杂度：O(n)
    leetcode testcases：无
    """
    if not node:
        return None
    if not node.next:  # 递归终止
        return [node.value]

    result = output_linkedlist_reversed_by_recursion(node.next)
    result.append(node.value)
    return result


def remove_kth_node_fromend(head, k):
    """删除链表倒数第k个节点
    时间复杂度：O(n)
    空间复杂度：O(k)
    leetcode testcases：https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
    """
    if not head or k < 1:
        return head

    pre_left = None  # 滑动窗口左边界：Kth_node - 1
    right = head  # 滑动窗口右边界

    # 初始化 滑动窗口
    while k > 1:
        if not right.next:
            raise IndexError("k is too large for linkedlist")
        right = right.next
        k -= 1

    # 移动滑动窗口，直至滑动窗口右边界到达最后一个节点
    while right.next:
        right = right.next
        pre_left = pre_left.next if pre_left else head

    # 找到 kth_node = left.next
    if not pre_left:  # kth_node为头节点
        head = head.next
    else:
        pre_left.next = pre_left.next.next
    return head
