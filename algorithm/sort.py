# -*- coding: utf-8 -*-
"""leetcode test

https://leetcode.cn/problems/sort-an-array/
"""


def selection_sort(arr):
    """
    时间复杂度：O(n^2) = (n-1)+(n-2)+…+1
    空间复杂度：O(1)
    """
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def bubble_sort(arr):
    """
    时间复杂度：O(n^2) = (n-1)+(n-2)+…+1
    空间复杂度：O(1)
    """
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_v1(arr):
    """没有逆序对时，就已达到有序，即可返回。

    时间复杂度：
         最好：O(n)
         最差：O(n^2) = (n-1)+(n-2)+…+1
    空间复杂度：O(1)
    """
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return arr
    return arr


def bubble_sort_v2(arr):
    """没有逆序对的局部，即有序，记录位置不再遍历。

    时间复杂度：
         最好：O(n)
         最差：O(n^2) = (n-1)+(n-2)+…+1
    空间复杂度：O(1)
    """
    last_swap = len(arr) - 1
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(last_swap):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                last_swap = j
        if -1 == swapped:
            return arr
    return arr


def insertion_sort(arr):
    """
    时间复杂度：
         最好：O(n)
         最差：O(n^2) = (n-1)+(n-2)+…+1
    空间复杂度：O(1)
    """
    for i in range(1, len(arr)):
        ele = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > ele):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = ele
    return arr


def insertion_sort_v1(arr):
    """
    时间复杂度：
         最好：
         最差：
    空间复杂度：
    """
    for i in range(1, len(arr)):
        ele = arr[i]
        j = i / 2
        while (j >= 0 and arr[j] > ele):
            arr[j + 1] = arr[j]
            # j =
        arr[j + 1] = ele
    return arr


def quick_sort(arr):
    """
    时间复杂度：
         最好：
         最差：
    空间复杂度：
    """
    pass


def merge_sort(arr):
    """
   时间复杂度：
        最好：
        最差：
   空间复杂度：
   """
    pass


if __name__ == "__main__":
    arr_list = [
        [],
        [1],
        [1, 2],
        [2, 1],
        [5, 2, 3, 1],
        [1, 2, 3, 4],
        [12, 34, 100, -10, 345, 49, 68, 0, 2435, 3546, 9, 45, 987, 12, 56, 8, 12, 67, 9, 3, 5],
        [17, 56, 71, 38, 61, 62, 48, 28, 57, 42]
    ]
    l = [1, 2, 3]
    for arr in arr_list:
        # print(bubble_sort(arr[:]))
        print(insertion_sort(arr[:]))
        # print(insertion_sort1(arr[:]))
