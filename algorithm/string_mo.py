# -*- coding: utf-8 -*-
"""字符串专题算法"""
import re
from math import ceil


def contain_sub_str(sub_str, str):
    """字符串是否包含子串
    时间复杂度：最好 O(m)｜最差 O(m*n)｜m=len(sub_str), n=len(str)
    空间复杂度：O(1)
    leetcode testcases：无
    """
    i, j = 0, 0
    while i < len(sub_str) and j < len(str):
        if sub_str[i] == str[j]:
            i, j = i + 1, j + 1
        else:
            i, j = 0, j - i + 1  # j从下一位开始匹配
    if i == len(sub_str):  # 子串开始位置
        return j - i
    else:
        return -1


def longest_not_duplicate_substring(str):
    """无重复字符的最长子串
    时间复杂度：O(n)
    空间复杂度：O(n)
    leetcode testcases：https://leetcode.cn/problems/wtcaE1/
    """
    if len(str) <= 1:
        return len(str)

    longest_len = 0
    char_position = {}  # 记录字符出现的最后一个位置
    left = 0  # 滑动窗口左端

    # 遍历一波str，就是滑动窗口右端位置。
    for right, char in enumerate(str):  # enumerate(可迭代对象)，返回 (下标, 元素)。此方法很快
        if char in char_position:  # 说明重复字符再次出现，需要移动滑动窗口的左端。
            left = max(left, char_position[char] + 1)  # 右端定为right的，最长不重复子串。通过移动左端寻找。
        char_position[char] = right  # 更新字符出现的最后一个位置
        longest_len = max(longest_len, right - left + 1)  # max(历史最长，当前最长)
    return longest_len


# longest_not_duplicate_substring("abba")


def is_prefix(s, words):
    """检查 字符串 是否为 字符串数组 前缀
    时间复杂度：O(n)
    空间复杂度：O(n)
    leetcode testcases：https://leetcode.cn/problems/check-if-string-is-a-prefix-of-array/
    """
    word = ""
    for i in words:
        word += i
        if s == word:
            return True
    return False


# print(is_prefix("a", ["aa", "aaaa", "banana"]))

def str_reverse(str):
    """字符串反转
    leetcode testcases：无
    """
    # 思路1：利用切片倒序。切片是浅复制，新瓶装旧酒。
    res = str[::-1]

    # 思路2：利用li.reverse()
    li = list(str)  # 转为list，每个元素是1个字符。
    li.reverse()  # reverse()是原地修改方法
    res = "".join(li)

    # 思路3：手动遍历
    res = ""
    for s in str:
        res = s + res
    return res


def str_reversal_by_word(str):
    """以单词级别 反转字符串
    leetcode testcases：无
    """
    # 先转化成单词list
    li = str.strip().split()  # .strip()：移除字符串头尾指定的字符，默认为空格
    # 反转list
    li.reverse()  # 原地修改方法
    return " ".join(li)


def longest_common_prefix_bysort(str_li):
    """字符串数组的最长公共前缀
    时间复杂度：sorted()排序O(nlogn) + O(m)
    空间复杂度：O(n)
    leetcode testcases：https://leetcode.cn/problems/longest-common-prefix/
    """
    if not str_li:
        return ""
    str_li = sorted(str_li)
    min, max = str_li[0], str_li[-1]
    for i in range(len(min)):
        if min[i] != max[i]:
            return min[:i]
    return min  # 正常退出


def longest_common_prefix_bytraverse(str_li):
    """字符串数组的最长公共前缀
    时间复杂度：O(m*n)
    空间复杂度：O(m)
    leetcode testcases：https://leetcode.cn/problems/longest-common-prefix/
    """
    if not str_li:
        return ""

    commom_prefix = ""
    for i in range(len(str_li[0])):
        char = str_li[0][i]
        for s in str_li:
            if i >= len(s) or s[i] != char:
                return commom_prefix
        commom_prefix += char
    return commom_prefix


def pickup_num_by_traverse(str):
    """从字符串中提取数字数组
    时间复杂度：O(n)
    空间复杂度：最大O(n)｜最小O(1)
    leetcode testcases：无
    """
    result = []
    i = 0
    while i < len(str):
        num = ""
        if str[i].isdigit():
            num += str[i]
            j = i + 1
            is_decimal = False  # 小数标志。因为小数点只能有一个。

            # j是：1）数字  2）第一次出现的小数点
            while j < len(str) and (str[j].isdigit() or (str[j] == "." and not is_decimal)):
                num += str[j]
                if str[j] == ".":
                    is_decimal = True
                j += 1
            result.append(float(num))
            i = j
        i += 1
    return result


# print(pickup_num_by_traverse("abcd.....123......和345.56jia567.2323.23jian345and23or345."))


def pickup_num_by_re(str):
    """从字符串中提取数字数组
   时间复杂度：最好=最差=平均=O(n)
   空间复杂度：最大O(n)｜最小O(1)
   leetcode testcases：无
    """
    # \d：1个数字。  .：除“\n”之外的任何单个字符。
    # ?：前面的内容0次或1次。  +：1次或多次。  *：0次或多次。
    res = re.findall(r"\d+\.?\d*", str)
    res = [float(x) for x in res]
    return res


def is_huiwen_by2pointer(str):
    """判断是否为 回文字符串
    时间复杂度：O(n)
    空间复杂度：O(1)
    leetcode testcases：https://leetcode.cn/problems/valid-palindrome/
    """
    i, j = 0, len(str) - 1
    while i < j:
        while i < j and not str[i].isalnum():  # .isalnum() = .isdigit() +.isalpha():
            i += 1
        while i < j and not str[j].isalnum():
            j -= 1
        if i <= j and str[i].lower() != str[j].lower():
            return False
        i, j = i + 1, j - 1
    return True


def is_huiwen_reverse(str):
    """判断是否为 回文字符串
    时间复杂度：O(n)
    空间复杂度：O(n)
    leetcode testcases：https://leetcode.cn/problems/valid-palindrome/
    """
    str = "".join([s.lower() for s in str if s.isalnum()])  # 数字+小写字符
    first_half = str[0:int(len(str) / 2)]  # int(5/2)=int(2.5)=2
    second_half = str[ceil(len(str) / 2):]  # b别用round()，round(10.5)=10....
    if first_half[::-1] == second_half:
        return True
    return False


# print(is_huiwen_reverse("A man, a plan, a canal: Panama"))
# print(round(10.5))

def shortest_distance_to_char(str, c):
    """字符的最短距离
    时间复杂度：O(n)
    空间复杂度：O(n)
    leetcode testcases：https://leetcode.cn/problems/shortest-distance-to-a-character/
    """
    length = len(str)
    result = [0] * length  # 默认最长

    left_close_c_index = -length  # 对于左侧没有c的情况，距离>=length不合法即可。
    # 第一次正序遍历，记录每个距离左侧最近的c的距离。
    for i, char in enumerate(str):  # enumerate(可迭代对象)，返回 (下标, 元素)。此方法很快
        if char == c:
            left_close_c_index = i  # 更新
        result[i] = i - left_close_c_index

    right_close_c_index = 2 * length  # 对于右侧没有c的情况，距离>=length不合法即可。
    # 第二次倒序遍历，记录每个距离右侧最近的c的距离。
    for i in range(length - 1, -1, -1):  # range倒序range(start, end, -1)：[start, -1)
        if str[i] == c:
            right_close_c_index = i
        result[i] = min(right_close_c_index - i, result[i])
    return result


print(shortest_distance_to_char("loveleetcode", "e"), len("loveleetcode"))


def first_uniq_char(s):
    """字符串中的第一个唯一字符
    时间复杂度：O(n)
    空间复杂度：O(1)
    leetcode testcases：https://leetcode.cn/problems/first-unique-character-in-a-string/
    """
    dic = {}
    # 遍历字符串，记录所有不重复字符串的位置，重复的字符串位置标为-1
    for i, char in enumerate(s):  # enumerate(可迭代对象)，返回 (下标, 元素)。此方法很快
        if char in dic:
            dic[char] = -1
        else:
            dic[char] = i
    # 找到第1个（dic是插入有序的）
    for i in dic:
        if dic[i] != -1:
            return dic[i]
    # 没有返回-1
    return -1
