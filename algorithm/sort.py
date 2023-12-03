# -*- coding: utf-8 -*-
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
    时间复杂度：最好 O(n)｜ 最差 O(n^2) = (n-1)+(n-2)+…+1
    空间复杂度：O(1)
    """
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr


def bubble_sort_v2(arr):
    """冒泡排序优化：没有逆序对的局部是部分有序的，记录位置不再遍历有序部分。
    时间复杂度：最好 O(n)｜ 最差 O(n^2) = (n-1)+(n-2)+…+1
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
    时间复杂度：最好 O(n)｜最差 O(n^2) = 1+2+...+(n-1)
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


def merge_sort(arr, start, end):
    """归并排序
    时间复杂度：O(nlogn)
    空间复杂度：O(n)
    """

    # 不断分组直至每组元素<=1个。
    if end <= start:
        return arr

    # 1.使组内自有序。
    mid = (start + end) // 2
    merge_sort(arr, start, mid)  # 不要mid-1，避免IndexError
    merge_sort(arr, mid + 1, end)

    # 2.进行组间排序。
    sorted_arr = []
    i, j = start, mid + 1
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            sorted_arr.append(arr[i])
            i += 1
        else:
            sorted_arr.append(arr[j])
            j += 1
    if i <= mid:
        sorted_arr.extend(arr[i:mid + 1])
    else:
        sorted_arr.extend(arr[j:end + 1])

    arr[start:end + 1] = sorted_arr  # 更新原数组
    return arr


def quick_sort(arr, start, end):
    """快速排序
    时间复杂度：最好 O(nlogn)｜最差 O(n^2)
    空间复杂度：最好 O(logn)｜最差 O(n)
    """
    if start >= end:  # 递归结束标志：边界异常/只剩一个元素。
        return arr

    pivot_index = random.randint(start, end)  # 随机选取pivot。randint取值范围：[start, end]
    pivot = arr[pivot_index]
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]  # 将基准值移至首位。
    i, j = start, end

    while i < j:
        # 下方两个while顺序不能变，必须先j后i。不然结果不对。
        while i < j and arr[j] >= pivot:  # 遍历右子序，从后至前，找到小于基准值的元素。
            j -= 1
        while i < j and arr[i] <= pivot:  # 遍历左子序，从前至后，找到大于基准值的元素。
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # 循环结束(i==j)：说明找到了pivot的正确位置j。令pivot的原始位置与正确位置进行交换。
    arr[j], arr[start] = pivot, arr[j]

    # 递归子序
    quick_sort(arr, start, j - 1)
    quick_sort(arr, j + 1, end)
    return arr


def find_Kth_by_quicksort(arr, start, end, k):
    """寻找第K大的数/前K大的数：基于快排
    时间复杂度：最好 O(n)｜最差 O(n^2)｜平均 O(nlog)
    空间复杂度：O()
    leetcode testcases：https://leetcode.cn/problems/xx4gT2/
    """
    if start >= end:
        return arr[-k]

    pivot_index = random.randint(start, end - 1)
    pivot = arr[pivot_index]
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
    i, j = start, end

    while i < j:
        # 下方两个while顺序不能变，必须先j后i。不然结果不对。
        while i < j and arr[j] >= pivot:  # 遍历右子序，从后至前，找到小于基准值的元素。
            j -= 1
        while i < j and arr[i] <= pivot:  # 遍历左子序，从前至后，找到大于基准值的元素。
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # 循环结束(i==j)：说明找到了pivot的正确位置j。令pivot的原始位置与正确位置进行交换。
    arr[j], arr[start] = arr[start], arr[j]

    if j == len(arr) - k:  # 找到了Kth
        return pivot

    find_Kth_by_quicksort(arr, start, j - 1, k)  # 没找到，继续递归左子序
    if j < len(arr) - k:  # 右子序
        find_Kth_by_quicksort(arr, j + 1, end, k)
    return arr[-k]


def find_Kth_by_mergesort(arr, start, end, k):
    """寻找第K大的数/前K大的数：基于归并排序
    时间复杂度：最好 O()｜最差 O()｜平均 O()
    空间复杂度：O()
    leetcode testcases：https://leetcode.cn/problems/xx4gT2/
    """
    if end <= start:
        return arr[-k]

    mid = (start + end) // 2
    find_Kth_by_mergesort(arr, start, mid, k)
    find_Kth_by_mergesort(arr, mid + 1, end, k)

    i, j = start, mid + 1
    sorted_arr = []
    while i <= mid and j <= end and len(sorted_arr) < k:  # 只排前K个元素即可
        if arr[i] <= arr[j]:
            sorted_arr.append(arr[i])
            i += 1
        else:
            sorted_arr.append(arr[j])
            j += 1
    if i <= mid and len(sorted_arr) < len(arr)-k:
        sorted_arr.extend(arr[i:i + (k - len(sorted_arr))])
    elif j <= end and len(sorted_arr) < k:
        sorted_arr.extend(arr[j:j + (k - len(sorted_arr))])

    arr[start:start + k + 1] = sorted_arr  # 更新原数组
    return arr[-k]


def find_Kth_by_orderedarr(arr, k):
    """寻找第K大的数/前K大的数：
    时间复杂度：最好 O()｜最差 O()｜平均 O()
    空间复杂度：O()
    leetcode testcases：https://leetcode.cn/problems/xx4gT2/
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
    arr_list = [
        [],
        [1],
        [1, 2],
        [2, 1],
        [5, 2, 3, 1],
        [1, 2, 3, 4],
        [3, 2, 1, 5, 6, 4],
        [3, 2, 3, 1, 2, 4, 5, 5, 6],
        [12, 34, 100, -10, 345, 49, 68, 0, 2435, 3546, 9, 45, 987, 12, 56, 8, 12, 67, 9, 3, 5],
        [17, 56, 61, 71, 38, 61, 62, 48, 28, 57, 61, 42],
        [-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]
    ]
    # for arr in arr_list:
    #     print(merge_sort(arr, 0, len(arr) - 1))
    arr = [3, 2, 1, 5, 6, 4]
    print(find_Kth_by_mergesort(arr, 2, 0, len(arr) - 1))
