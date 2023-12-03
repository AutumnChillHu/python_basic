# -*- coding: utf-8 -*-

def binary_search(arr, target):
    """有序数组，返回下标。
    时间复杂度： O(logn)
    空间复杂度：O(1)
    leetcode testcases：https://leetcode.cn/problems/binary-search/
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (right + left) // 2  # //：整除，只保留整数位。
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


def find_missing_num(arr):
    """有序数组[0,1,2,...,i-1,i+1...,n-1]，缺失了数字i，返回i。若无缺失返回n。
    时间复杂度：O(logn)
    空间复杂度：O(1)
    leetcode testcases：无
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid:
            left = mid + 1
        elif arr[mid] > mid:  # 缺失数字出现在左部分
            right = mid - 1
        else:
            print("异常情况，原数组异常")
    return left  # left = right+1


def binary_search_first(arr, target):
    """有序数组，返回第一个匹配元素的下标。
    时间复杂度：O(logn)
    空间复杂度：O(1)
    leetcode testcases：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
    """
    if not arr:
        return -1

    left, right = 0, len(arr) - 1
    while left < right:  # 当left=right时, 就退出循环。否则while left <= right，由于right=mid，可能导致left=right，永远无法退出循环。
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    if arr[right] == target:  # right==left
        return right
    return -1


# print(binary_search_first([5, 7, 7, 8, 8, 10], 5))


def binary_search_last(arr, target):
    """有序数组，返回最后一个匹配元素的下标。
    时间复杂度：O(logn)
    空间复杂度：O(1)
    leetcode testcases：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
    """
    if not arr:
        return -1

    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2 + 1  # 整除是向下取整。这里+1，避免left = mid，一直无法退出循环的情况。
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            left = mid

    # 可能场景：已经找到最后一个，进入下一轮循环，mid会+1，arr[mid]>target,right-1,所以right的值是正确。
    if arr[right] == target:  # left>=right，退出循环。
        return right
    return -1


# print(binary_search_last([5, 7, 7, 8, 8, 10], 8))

def two_nums_sum(arr, target):
    """数组有序，查找和为s的两个数字。
    时间复杂度：O(n)
    空间复杂度：O(1)
    leetcode testcases：https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/
    """
    i, j = 0, len(arr) - 1
    while i < j:
        if (arr[i] + arr[j]) < target:
            i += 1
        elif (arr[i] + arr[j]) > target:
            j -= 1
        else:
            return [arr[i], arr[j]]
    return None


def min_in_parted_sorted_array(arr):
    """寻找旋转排序数组中的最小值
    时间复杂度：O(logn)
    空间复杂度：O(1)
    leetcode testcases：https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/solutions/9474/154-find-minimum-in-rotated-sorted-array-ii-by-jyd/
    """
    i, j = 0, len(arr) - 1
    while i < j:  # 等于退出
        mid = (i + j) // 2
        if arr[mid] > arr[j]:  # 最小值出现在右边 (mid, j]
            i = mid + 1
        elif arr[mid] < arr[j]:  # 最小值出现在左边 [0, mid]
            j = mid
        else:  # j!=mid，所以j-1
            j -= 1
    return arr[i]
