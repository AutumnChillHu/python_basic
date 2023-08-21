# -*- coding: utf-8 -*-
"""
wiki：https://janineee.atlassian.net/wiki/spaces/JW/pages/9371780
leetcode testcases：https://leetcode.cn/problems/sort-an-array/
"""
import random


def selection_sort(arr):
    """选择排序
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
    """冒泡排序
    时间复杂度：O(n^2) = (n-1)+(n-2)+…+1
    空间复杂度：O(1)
    """
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_v1(arr):
    """冒泡排序优化：没有逆序对时，已达到有序，即可返回。
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
    """冒泡排序优化：没有逆序对的局部是部分有序的，记录位置不再遍历有序部分。
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
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                last_swap = j
        if not swapped:
            return arr
    return arr


def insertion_sort(arr):
    """插入排序
    时间复杂度：
         最好：O(n)
         最差：O(n^2) = 1+2+...+(n-1)
    空间复杂度：O(1)
    """
    for i in range(1, len(arr)):
        item = arr[i]
        j = i - 1
        while (j >= 0 and item < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item
    return arr


def quick_sort(arr, start, end):
    """快速排序
    时间复杂度：
         最好：O(nlogn)
         最差：O(n^2)
    空间复杂度：
        最好：O(logn)
        最差：O(n)
    """
    if start >= end:  # 递归结束标志：边界异常/只剩一个元素。
        return arr

    # 随机选取pivot
    pivot_index = random.randint(start, end - 1)  # randint取值范围：[start, end]
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]  # 将基准值移至首位。
    pivot = arr[start]
    i, j = start, end

    while i < j:
        # 下方两个while顺序不能变，必须先j后i。不然结果不对。
        while arr[j] >= pivot and i < j:  # 遍历右子序，从后至前，找到小于基准值的元素。
            j -= 1
        while arr[i] <= pivot and i < j:  # 遍历左子序，从前至后，找到大于基准值的元素。
            i += 1

        arr[i], arr[j] = arr[j], arr[i]

    # 当i=j，左右坐标重合之时，循环结束，说明找到了pivot的正确位置j。遍历结束。令pivot的原始位置与正确位置进行交换。
    arr[j], arr[start] = pivot, arr[j]

    # 递归子序
    quick_sort(arr, start, j - 1)
    quick_sort(arr, j + 1, end)
    return arr


def merge_sort(arr, start, end):
    """归并排序
    时间复杂度：O(nlogn)
    空间复杂度：O(n)
    """

    # 不断分组直至每组元素<=1个。
    if end <= start:
        return arr

    # 1.使两组各自有序。
    mid = (start + end) // 2 + 1
    merge_sort(arr, start, mid - 1)
    merge_sort(arr, mid, end)

    # 2.进行组间排序。
    sorted_arr = []
    i, j = start, mid
    while i < mid or j <= end:
        # or的两个条件的先后顺序不能改变，否则有可能出现j超出范围的错误。
        # j超标且i还剩余的情况 or ij都在范围内且i更小
        if j > end or (i < mid and arr[i] <= arr[j]):
            sorted_arr.append(arr[i])
            i += 1
        else:
            sorted_arr.append(arr[j])
            j += 1
    arr[start:end + 1] = sorted_arr
    return arr


if __name__ == "__main__":
    arr_list = [
        [],
        [1],
        [1, 2],
        [2, 1],
        [5, 2, 3, 1],
        [1, 2, 3, 4],
        [12, 34, 100, -10, 345, 49, 68, 0, 2435, 3546, 9, 45, 987, 12, 56, 8, 12, 67, 9, 3, 5],
        [17, 56, 61, 71, 38, 61, 62, 48, 28, 57, 61, 42],
        [-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]
    ]

    # for arr in arr_list:
    #     # print(merge_sort(arr, 0, len(arr) - 1))
    #     print(quick_sort(arr, 0, len(arr) - 1))

    li = [3, 2, 1, 5, 6, 4]
    print(merge_sort(li, 0, len(li) - 1))
    print(li)
