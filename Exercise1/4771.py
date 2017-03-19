# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
from log_api import log


class Solution():
    def solve(self, A):
        result = {}
        for i in range(0, 10):
            result[i] = 0
        for str in A:
            for c in str:
                i = int(c)
                result[i] += 1
        return result


log(Solution().solve(['12', '34', '567', '36', '809', '120']))
