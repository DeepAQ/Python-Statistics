# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
from scipy.stats import chi2

from log_api import log


class Solution():
    def solve(self):
        data = ((154, 132), (180, 126), (104, 131))
        total_x = (286, 306, 235)
        total_y = (438, 389)
        total = 827
        c2 = 0
        for i in range(0, 3):
            for j in range(0, 2):
                t = total_x[i] * total_y[j] * 1.0 / total
                c2 += (data[i][j] - t) ** 2 / t
        d = chi2.ppf(0.95, 2)
        return [2, round(c2, 2), c2 < d]


'''
The table below summaries a data set that examines the response of a random sample of college graduates and non-graduate on the topic of oil drilling. Complete a chi-square test for test data to check whether there is a statistically significant difference in responses from college graduates and non-graduates.

College Grad?	Yes	No	Total
Support	154	132	286
Oppose	180	126	306
Do not know	104	131	235
Total	438	389	827

Output Description

[degree-of-freedom-of-distribution, statistical values, conclusion],'degree-of-freedom-of-distribution' and 'statistical values' are accurate to the second decimal place, 'conclusion' is True, which means the H0 is accepted, or False
'''
log(Solution().solve())
