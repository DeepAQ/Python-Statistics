# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
import math
from scipy.stats import t

from log_api import log


class Solution():
    def solve(self):
        d = t.ppf(0.05, 24)
        sv = (7.73 - 8) / 0.77 * math.sqrt(25)
        con = sv > d
        return [24, round(sv, 2), con]


'''
New York is known as "the city that never sleeps". A random sample of 25 New Yorkers were asked how much sleep they get per night. Statistical summaries of these data are shown below. Do these data provide strong evidence that New Yorkers sleep less than 8 hours per night on average?

Null-hypothesis is H0: u=8, and alpha is 0.05

n	mean	stand-variance	min	max
25	7.73	0.77	6.17	9.78


Extra:

(1) If you were to construct a 90% confidence interval that corresponded to this hypothesis test, would you expect 8 hours to be in the interval? Explain your reasoning.
'''
log(Solution().solve())
