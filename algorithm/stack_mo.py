# -*- coding: utf-8 -*-
def right_brackets(s):
    """括号是否有效（只有括号）
    时间复杂度：O(n)
    空间复杂度：O(n)
    leetcode testcases：https://leetcode.cn/problems/valid-parentheses/
    """
    dic = {")": "(", "]": "[", "}": "{"}
    bracket_stack = []

    for i in s:
        if i in dic.values():
            bracket_stack.append(i)
            continue
        elif i in dic.keys():
            if not bracket_stack or bracket_stack.pop() != dic[i]:
                return False
    if bracket_stack:
        return False
    return True


print(right_brackets("([)]"))


def brackets_maxdepth(s):
    """有效括号的最大深度
    时间复杂度：O(n)
    空间复杂度：O(n)
    leetcode testcases：https://leetcode.cn/problems/maximum-nesting-depth-of-the-parentheses/
    """
    bracket_stack = []
    max_depth = 0
    for i in s:
        if i == "(":
            bracket_stack.append(i)
            max_depth = max(len(bracket_stack), max_depth)
        elif i == ")":
            bracket_stack.pop()
    return max_depth
