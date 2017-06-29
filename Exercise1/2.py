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


log(Solution().solve(['123', '232', '4556554', '12123', '3443', '1314131']))
