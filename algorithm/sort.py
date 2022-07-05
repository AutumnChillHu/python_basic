# -*- coding: utf-8 -*-

def select_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def select_sort1(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def bubble_sort():
    pass


if __name__ == "__main__":
    arr_list = [
        [],
        [1],
        [5, 2, 3, 1],
        [12, 34, 100, -10, 345, 49, 68, 0, 2435, 3546, 9, 45, 987, 12, 56, 8, 12, 67, 9, 3, 5]
    ]
    for arr in arr_list:
        print(select_sort(arr))
    print(arr_list)
