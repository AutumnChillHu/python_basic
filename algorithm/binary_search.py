# -*- coding: utf-8 -*-
"""
wiki：https://janineee.atlassian.net/wiki/spaces/JW/pages/9568326
"""


def binary_search(arr, target):
    """二分查找
    时间复杂度：
         最好：O(1)
         最差：O(logn)
         平均：O(logn)
    空间复杂度：O(1)
    leetcode testcases：https://leetcode.cn/problems/binary-search/
    """
    left, right = 0, len(arr) - 1
    while left <= right:  # 只有right>left时才算异常
        mid = (right + left) // 2  # //：整除，向下取整，只保留整数位。
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    arr = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(binary_search(arr, target))
