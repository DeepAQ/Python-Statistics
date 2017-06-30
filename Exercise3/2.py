# -*- coding:utf-8 -*-

from scipy.stats import t

from log_api import log


class Solution():
    def solve(self):
        mean = (18.985 + 21.015) / 2
        sd = (21.015 - mean) * 6 / -t.ppf(0.025, 35)
        return [round(mean, 2), round(sd, 2)]


'''
A 95% confidence interval for a population mean, u, is given as (18.985, 21.015). This confidence interval is based on a simple random 
samples of 36 observations. Calculate the sample mean and standard deviation. Assume that all conditions necessary for inference are 
satisfied. Use the t-distribution in any calculations.

Output Description

[mean, standard deviation], accurate to the second decimal place
'''
log(Solution().solve())
