# -*- coding: utf-8 -*-

def select_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


def bubble_sort():
    pass


if __name__ == "__main__":
    for i in range(2):
        print(i)
