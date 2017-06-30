# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
import math

from scipy.stats import norm

from log_api import log


class Solution:
    def solve(self):
        mean = 8.5
        count = 3600
        var = 25
        lower = mean - (math.sqrt(var) * norm.ppf(0.025)) / math.sqrt(count)
        upper = mean + (math.sqrt(var) * norm.ppf(0.025)) / math.sqrt(count)
        return [lower, upper]


'''
随着中国经济发展，人们生活质量相应提升，但睡眠质量却并不乐观。据《2016中国睡眠指数报告》显示，中国人平均睡眠时长为8.5小时， 这是从3600份问卷统计得到的结果。另外报告指出，中国人睡眠时长符合方差为25的正态分布，试写solve函数估计中国人睡眠时长的置信区间(置信水平为95%)

Output Description

[lower,upper]分别代表睡眠时长的估计下限与上限
'''
log(Solution().solve())
