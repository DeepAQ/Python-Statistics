# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
import math

from scipy.stats import t

from log_api import log


class Solution():
    def solve(self):
        d = t.ppf(0.025, 21)
        mean = 52.1 - 27.1
        sd = math.sqrt(45.1 ** 2 + 26.4 ** 2)
        sv = mean / sd * math.sqrt(22)
        con = sv < d
        return [21, round(sv, 2), con]


'''
A group of researchers are interested in the possible effects of distracting stimuli during eating, such as an increase or decrease in the amount of food consumption. To test this hypothesis, they monitored food intake for a group of 44 patients who were randomised into two equal groups. The treatment group ate lunch while playing solitaire, and the control group ate lunch without any added distractions. Patients in the treatment group ate 52.1 grams of biscuits, with a standard deviation of 45.1 grams, and patients in the control group ate 27.1 grams of biscuits with a standard deviation of 26.4 grams. Do these data provide convincing evidence that the average food intake is different for the patients in the treatment group? Assume the conditions for inference are satisfied.

Null hypothesis is H0: u_t - u_c = 0, alpha is 0.05

Output Description

[degree-of-freedom-of-distribution, statistical values, conclusion],'degree-of-freedom-of-distribution' and 'statistical values' are accurate to the second decimal place, 'conclusion' is True, which means the H0 is accepted, or False
'''
log(Solution().solve())
