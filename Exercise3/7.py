# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
import math

from scipy.stats import t

from log_api import log


class Solution():
    def solve(self):
        d = t.ppf(0.05, 19)
        sv = (4.6 - 5) / 2.2 * math.sqrt(20)
        con = sv > d
        return [19, round(sv, 2), con]


'''
Georgianna claims that in a small city renowned for its music school, the average child takes at least 5 years of piano lessons. We have a random sample of 20 children from the city with a mean of 4.6 years of piano lessons and a standard deviation of 2.2 years. Evaluate Georgianna's claims using a hypothesis test. alpha is 0.05.



Extra:

(1) Construct a 95% confidence interval for the number of years students in this city takes piano lessons and interpret it in context of the data.

(2) Do your results from the hypothesis test and the confidence interval agree? Explain your reasoning.

Output Description

[degree-of-freedom-of-distribution, statistical values, conclusion],'degree-of-freedom-of-distribution' and 'statistical values' are accurate to the second decimal place, 'conclusion' is True, which means the H0 is accepted, or False
'''
log(Solution().solve())
