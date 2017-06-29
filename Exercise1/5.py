# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
from log_api import log


class Solution():
    def solve(self, A):
        # call function prime
        result = []
        for num in A:
            if self.prime(num):
                result.append(num)
        return result

    # judge whether x is prime or not
    def prime(self, x):
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True


log(Solution().solve([23, 45, 76, 67, 17]))
