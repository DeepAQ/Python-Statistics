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


'''
完成函数solve，判断传入的整数列表A中的数字是否是素数，并将所有的素数保存到另一个列表中并返回

Input / Output

Input Example

[23,45,76,67,17]

Input Description

一个含素数和非素数的多个整数列表

Output Example

[23,67,17]

Output Description

素数组成的列表
'''
log(Solution().solve([23, 45, 76, 67, 17]))
