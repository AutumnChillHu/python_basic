# -*- coding: utf-8 -*-
"""leetcode testcases 选取第K大/前K个元素:https://leetcode.cn/problems/xx4gT2/"""

import random


def find_Kth_by_quicksort(arr, start, end, k):
    """寻找第K大的数/前K大的数：基于快排"""
    if start >= end:
        return arr

    pivot_index = random.randint(start, end - 1)
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
    pivot = arr[start]
    i, j = start, end

    while i < j:
        while arr[j] >= pivot and i < j:
            j -= 1
        while arr[i] <= pivot and i < j:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[start] = arr[start], arr[j]
    if j == len(arr) - k:  # 第k大 = arr[-k] = arr[len-k]
        return pivot
    find_Kth_by_quicksort(arr, start, j - 1, k)  # 左子序
    if j < len(arr) - k:  # 右子序
        find_Kth_by_quicksort(arr, j + 1, end, k)
    return arr[-k], arr


def find_Kth_by_mergesort(arr, start, end, k):
    """寻找第K大的数/前K大的数：基于归并排序"""
    if end <= start:
        return arr[k - 1]

    mid = (start + end) // 2 + 1
    find_Kth_by_mergesort(arr, start, mid - 1, k)
    find_Kth_by_mergesort(arr, mid, end, k)

    i, j = start, mid
    sorted_arr = []  # 倒序排列元素
    while (i < mid or j <= end) and len(sorted_arr) < k:  # 只排前K个元素即可
        if j > end or (i < mid and arr[i] >= arr[j]):
            sorted_arr.append(arr[i])
            i += 1
        else:
            sorted_arr.append(arr[j])
            j += 1
    end_index = start + k if len(sorted_arr) == k else end + 1
    arr[start: end_index] = sorted_arr
    return arr[k - 1]


def find_Kth_by_orderedarr(arr, k):
    """寻找第K大的数/前K大的数：
    维护一个由大到小的有序数组，遍历一趟。
    """
    ordered_arr = [None] * (k + 1)  # 数组长为k+1，方便第k个元素后移，循环里面不用单独处理。
    for item in arr:
        i = k - 1  # i指向第K个元素
        # 插入排序思想维护：向前遍历，元素后移，找到正确位置后插入。
        while i >= 0 and (ordered_arr[i] == None or item > ordered_arr[i]):
            ordered_arr[i + 1] = ordered_arr[i]
            i -= 1
        ordered_arr[i + 1] = item
    return ordered_arr[k - 1]


if __name__ == "__main__":
    arr = [3, 2, 1, 5, 6, 4]

    print(find_Kth_by_mergesort(arr, 0, len(arr) - 1, 2))
