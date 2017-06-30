# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''

from scipy.stats import chi2

from log_api import log


class Solution():
    def solve(self):
        data = [43, 21, 35]
        d = chi2.ppf(0.95, len(data) - 1)
        mean = sum(data) / len(data)
        sv = 0
        for x in data:
            sv += (x - mean) ** 2 * 1.0 / mean
        con = sv < d
        return [len(data) - 1, round(sv, 2), con]


'''
Rock-paper-scissors is a hand game played by two or more people where players choose to sign either rock, paper or scissors with their hands. For your statistics class project, you want to evaluate whether players choose between these three options randomly, or if certain options are favoured above others. You ask two friends to play rock-paper-scissors and count the time each option is played. The following table summaries the data:

Rock	Paper	Scissors
43	21	35

Use these data to evaluate whether players choose between these three options randomly, or if certain options are favored above others. alpha is 0.05.

Output Description

[degree-of-freedom-of-distribution, statistical values, conclusion],'degree-of-freedom-of-distribution' and 'statistical values' are accurate to the second decimal place, 'conclusion' is True, which means the H0 is accepted, or False
'''
log(Solution().solve())
