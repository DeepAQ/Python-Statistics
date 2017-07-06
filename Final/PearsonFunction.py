# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
import numpy as np
from scipy.stats import t, pearsonr, beta

from log_api import log


class Solution():
    def solve(self, x, y):
        if (not x and not y) or len(x) != len(y):
            return [None, None]
        n = len(x)
        x_mean = np.mean(x)
        y_mean = np.mean(y)
        x_delta = [xi - x_mean for xi in x]
        y_delta = [yi - y_mean for yi in y]
        sum_xy = np.sum([x_delta[i] * y_delta[i] for i in range(0, n)])
        sum_x2 = np.sum([xd ** 2 for xd in x_delta])
        sum_y2 = np.sum([yd ** 2 for yd in y_delta])
        r_val = sum_xy / np.sqrt(sum_x2) / np.sqrt(sum_y2)
        if abs(r_val) == 1.0:
            p_val = 0.0
        else:
            t2 = r_val ** 2 * ((n - 2) / ((1.0 - r_val) * (1.0 + r_val)))
            p_val = 1 - beta.sf((n - 2) / (n - 2 + t2), 0.5 * (n - 2), 0.5)
        return [round(r_val, 6), round(p_val, 6)]


'''
利用python实现简化版皮尔森相关系数计算函数
注意事项：
1）scipy包只能使用scipy.x.ppf或scipy.x.sf函数
2）x,y为空时，返回值为[None,None]
3）结果保留6位小数点

Input Description

x : 一维数组；y : 一维数组，且x、y长度相同

Output Description

[r-val,p-value]分别代表皮尔森相关系数、检验结果P值
'''
log(Solution().solve([1, 2, 3], [2, 2, 3]))
