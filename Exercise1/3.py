# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
import numpy as np

from log_api import log


class Solution():
    def solve(self, A):
        return np.poly1d(A) * np.poly1d(np.array([2.0, 0.0, -1.0, 1.0]))


log(Solution().solve(np.array([1.0, 2.0, 1.0])))
