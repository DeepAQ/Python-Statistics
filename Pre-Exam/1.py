# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
import numpy as np

from log_api import log


class Solution():
    def solve(self):
        # 1 - P(X = 0) >= 0.98
        # 1 - e^(-lambda) >= 0.98
        # lambda >= -ln(0.02)
        l = - np.log(0.02)
        return np.ceil(l)


'''
假定一块蛋糕上的葡萄干粒数服从泊松分布，如果想让每块蛋糕上至少有一粒葡萄干的概率大于等于0.98，蛋糕上葡萄干的平均粒数应该是多少？

Output Example

1

Output Description

num_of_grape, int类型数字
'''
log(Solution().solve())
