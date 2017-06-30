# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
import math

from scipy.stats import norm

from log_api import log


class Solution():
    def solve(self):
        return math.floor(2 * 94 * 94 / ((40 / (norm.ppf(0.9) + norm.ppf(0.975))) ** 2))


'''
A large farm wants to try out a new type of fertilizer to evaluate whether it will improve the farm's corn production. The land is broken into plots that produce an average of 1.215 pounds of corn with a standard deviation of 94 pounds per plot. The owner is interested in detecting any average difference of at least 40 pounds per plot. How many plots of land would be needed for the experiment if the desired power level is 90%? Assume each plot of land gets treated with either the current fertilizer or the new fertilizer.

Output Description

plot_num, int type
'''
log(Solution().solve())
