# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
from log_api import log


class Solution():
    def solve(self, A):
        result = {}
        for str in A:
            result[str] = result.get(str, 0) + 1
        return result


log(Solution().solve(['apple', 'banana', 'cherry', 'pineapple', 'banana', 'peach', 'pear', 'peach', 'cherry']))
