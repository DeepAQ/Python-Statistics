# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
from log_api import log


class Solution():
    def solve(self, A):
        result = []
        for str in A:
            if self.isPalindrome(str):
                result.append(str)
        return result

    def isPalindrome(self, x):
        return x == x[::-1]


'''
对于一个包含一系列数字字符串的列表，寻找其中的回文串存入一个列表中并返回
Input / Output

Input Example

['123', '232', '4556554', '12123', '3443','1314131']

Input Description

一个包含一系列数字字符串的列表

Output Example

['232', '4556554', '3443','1314131']

Output Description

仅包含回文串的列表
'''
log(Solution().solve(['123', '232', '4556554', '12123', '3443', '1314131']))
