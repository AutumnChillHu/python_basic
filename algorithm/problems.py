# -*- coding: utf-8 -*-
import functools
import os
import random
import re


def redpacket_by_average(money, n):
    """发红包-二倍均值法
    时间复杂度：最好 O(n)
    空间复杂度：O(n)
    leetcode testcases：无
    """
    if money < n * 0.01 or n < 1:
        print("not enough money or not enough people")
        return None

    # 转换成 分为单位，生成随机整数即可。
    # random.uniform(a, b)：随机返回区间[a,b]之间的一个小数，很长位数，还要涉及四舍五入，不够精准。
    left_money = money * 100
    result = []
    while n > 1:
        max_money = min(int((left_money / n) * 2), left_money - (n - 1))  # 限制蠛个人最大金额
        one_result = random.randint(1, max_money)  # random.randint(a, b) 返回[a, b]区间内的一个随机整数
        result.append(one_result)
        n = n - 1
        left_money -= one_result
    result.append(left_money)
    return [i / 100 for i in result]


def redpacket_by_cut(money, n):
    """发红包-线段切割法
    时间复杂度：O(nlogn)      [ O(nlogn) > O(n) ]
              list.sort()采用混合排序：规模小用插入排序O(n)，规模大用快速排序O(nlogn)。
              n次循环为O(n)
    空间复杂度：O(n)
    leetcode testcases：无
    """
    if money < n * 0.01 or n < 1:
        print("not enough money for current people")
        return None

    string_tocut = [0]  # 线段起点
    indexs = set()  # 为了提高性能：基于hashmap实现的数据结构，后面用in判断会更快
    while n > 1:
        # 转换成分为单位，所以相邻节点最小长度为1，即能满足每人最少拿到1分钱。
        cut_point = random.randint(1, money * 100 - 1)  # random.randint(a, b) 返回[a, b]区间内的一个随机整数

        # 切割点重复了，就重新再切一次
        if cut_point in indexs:  # indexs是set()基于hashmap实现的数据结构，用in判断会更快
            continue
        indexs.add(cut_point)
        string_tocut.append(cut_point)
        n = n - 1

    string_tocut.append(money * 100)  # 线段终点
    string_tocut.sort()
    return [(string_tocut[i] - string_tocut[i - 1]) / 100 for i in range(1, len(string_tocut))]


def vaild_codelines(file_path):
    """统计文件有效代码行
    时间复杂度：O(n)
    空间复杂度：O(1)
    leetcode testcases：无
    """
    count = 0
    with open(file_path, 'r') as file:  # with-as语法糖：进入with执行file.open()；退出with执行file.close()。
        nextline_is_comment = False
        for line in file:
            line = line.strip()
            # 1)空行、2)注释行#、3)单行的注释段 '''line'''/"""line"""
            if not line or line.startswith("#") or re.findall(r"\"\"\".*\"\"\"", line) or re.findall(
                    r"\'\'\'.*\'\'\'", line):  # .：匹配除\n之外的任意单个字符。  *：0次或多次。
                continue
            elif not nextline_is_comment and (line.startswith("\"\"\"") or line.startswith("'''")):  # 多行注释段开始
                nextline_is_comment = True
            elif nextline_is_comment and (line.endswith("\"\"\"") or line.endswith("'''")):  # 多行注释段结束
                nextline_is_comment = False
            elif nextline_is_comment:  # 多行注释段的注释
                continue
            elif not nextline_is_comment:
                count += 1
    return count


# print(vaild_codelines("/Users/mo/Documents/python_basic/algorithm/__init__.py"))


def count_and_say(n):
    """外观数列
    时间复杂度：O(mn)
    空间复杂度：O(m)
    leetcode testcases：https://leetcode.cn/problems/count-and-say/description/
    """
    if n < 1:
        return ""

    s = "1"  # 第一个字符串为"1"
    for seq in range(2, n + 1):  # 从第二个数字开始
        curr_char = s[0]
        curr_cnt = 0
        new_s = ""
        for i in s:
            if i == curr_char:
                curr_cnt += 1
            else:
                new_s += str(curr_cnt) + curr_char
                curr_char = i
                curr_cnt = 1
        s = new_s + str(curr_cnt) + curr_char
    return s


def soomth_cards(cards):
    """扑克牌中的顺子
    时间复杂度：O(n)
    空间复杂度：O(n)
    leetcode testcases：无
    """
    cards_norepeat = set()
    mini, maxi = 99, -1
    for card in cards:
        if card == 0:  # 遇到大小王跳过
            continue
        if card in cards_norepeat:  # 出现除0外的重复牌，一定不是顺子
            return False
        cards_norepeat.add(card)  # 记录不重复的牌
        mini, maxi = min(mini, card), max(maxi, card)  # 更新最大、最小牌
        if (maxi - mini) > 4:  # 除0外，牌差值超限，max-min>4。
            return False
    return True


def fibonacci_by_recursion(n):
    """fibonacci数列
    时间复杂度：O(2^n)
    空间复杂度：O(1)
    leetcode testcases：无
    """
    if n <= 0:
        return None
    if n <= 2:  # 递归停止
        return (n - 1)
    return fibonacci_by_recursion(n - 1) + fibonacci_by_recursion(n - 2)


def fibonacci_by_iteration(n):
    """fibonacci数列
    时间复杂度：O(n)
    空间复杂度：O(1)
    leetcode testcases：无
    """
    if n < 3:
        return n - 1
    a, b = 0, 1
    # n=3进入迭代，所以range(3, x)，迭代一次就够了，推算出x=3+1 => n+1
    for i in range(3, n + 1):  # range(1, 0)、range(1, 1) ：都不会进去循环
        a, b = b, a + b
    return b


# print(fibonacci_by_recursion(7))
# print(fibonacci_by_iteration(7))


def frog_jump_by_recursion(n):
    """青蛙跳台阶
    时间复杂度：O(2^n)
    空间复杂度：O(1)
    leetcode testcases：https://leetcode.cn/problems/climbing-stairs/
    """
    if n < 3:
        return n
    return (frog_jump_by_recursion(n - 1) + frog_jump_by_recursion(n - 2))


def frog_jump_by_iteration(n):
    """青蛙跳台阶
    时间复杂度：O(n)
    空间复杂度：O(1)
    leetcode testcases：https://leetcode.cn/problems/climbing-stairs/
    """
    if n <= 0:
        return 1
    a, b = 1, 1
    # 2级台阶进入迭代，所以range(2, x)，迭代一次就够了，推算出x=2+1 => n+1
    for i in range(2, n + 1):  # range(2, 2)、range(2, 1) ：都不会进去循环
        a, b = b, a + b
    return b


# print(frog_jump_by_iteration(2))


def find_and_change_filename(root):
    """更改目录下所有文件的名字
    时间复杂度：O()
    空间复杂度：O()
    leetcode testcases：无
    """
    # path：当前目录的完整路径。是一个string。
    # dirs：当前目录下的所有文件夹，是一个list，每个元素为文件名string
    # files：当前目录下的所有文件，是一个list，每个元素为文件名string
    # 通过遍历就是一层一层进去
    for path, dirs, files in os.walk(root):
        for filename in files:
            if filename.endswith(".txt"):
                os.rename(filename, filename.split(".txt")[0] + ".pdf")


# find_and_change_filename("/Users/mo/Documents/python_basic")


def odd_before_even(arr):
    """奇数位于偶数前面
    时间复杂度：O(n)
    空间复杂度：O(1)
    leetcode testcases：无
    """
    i, j = 0, len(arr) - 1
    while i < j:
        while i < j and arr[i] % 2 == 1:  # i是奇数，前进
            i += 1
        while i < j and arr[j] % 2 == 0:  # j遇到偶数，前进
            j -= 1
        if i < j:  # 出现逆序情况
            arr[i], arr[j] = arr[j], arr[i]
            i -= 1
            j -= 1
    return arr


def if_stack_pop_right(pushed, popped):
    """给一个入栈队列，给一个出栈队列，判断是否是正确
    时间复杂度：O(n)
    空间复杂度：O(n)
    leetcode testcases：无
    """
    if len(pushed) != len(popped):
        return False

    length = len(pushed)
    for i in range(length):
        if pushed[i] != popped[length - 1 - i]:
            return False
    return True


def search_matrix(matrix, target):
    """有序不重复二维数组的查找
    时间复杂度：O(m+n)
    空间复杂度：O(1)
    leetcode testcases：https://leetcode.cn/problems/search-a-2d-matrix/
    """
    if not matrix or not matrix[0]:
        return False

    i, j = 0, len(matrix[0]) - 1  # 右上角元素
    while i < len(matrix) and j >= 0:
        if matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] < target:
            i += 1
        else:
            return True
    return False
