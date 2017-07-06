# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
from urllib2 import urlopen

import numpy as np
import pandas as pd
from scipy.stats import t, f

from log_api import log


class Solution():
    def solve(self):
        url = 'http://py.mooctest.net:8081/dataset/population/population_work.csv'
        df = pd.read_csv(urlopen(url), encoding='gbk', skiprows=range(0, 4), header=None)
        adult_rate = df[2] / df[1] * 100
        work_rate = df[4] / df[3]
        jobless_rate = df[7] / df[3]
        n = len(adult_rate)

        mean = np.mean(adult_rate)
        sd = np.std(adult_rate, ddof=1)
        mean_delta = sd / np.sqrt(n) * t.ppf(0.95, n - 1)

        var1 = np.var(work_rate)
        var2 = np.var(jobless_rate)
        var_lower = var1 / var2 / f.ppf(0.95, n - 1, n - 1)
        var_upper = var1 / var2 / f.ppf(0.05, n - 1, n - 1)
        return [[mean - mean_delta, mean + mean_delta], [var_lower, var_upper]]


'''
人口普查是一项重要的国情调查，对于国家管理、制定各项方针政策具有重要的意义，中国最早的一次人口普查在西汉汉平帝元始二年进行，而自中华人民共和国建国以来分别在1953、1964、1982、1990、2000和2010年进行了共六次人口普查，其中第六次人口普查分别涉及到了人口增长、家庭户人口、性别构成、年龄构成、民族构成、受教育程度、城乡人口、人口流动性等八方面。现有关于《各地区分性别的16岁及以上人口的就业状况》的数据，现定义成年人比率=16岁及以上人口/总人口，就业率=就业人口/经济活动人口，失业率=失业人口/经济活动人口，以北京为例其成年人比率=1672749/1849475=0.9044，就业率=977387/1020455=0.9578，失业率=43068/1020455=0.0422，请利用Python代码完成如下问题：
1）以各地区数据为代表，计算成年人比率均值的置信区间，置信水平为90%，假设成年人比率符合正态分布
2）以各地区数据为代表，计算就业率与失业率的方差比的置信区间，置信水平为90%，假设就业率与失业率辆样本相互独立，且各自符合正态分布

Output Example

[[mean_lower, mean_upper], [variance_lower, variance_upper]]

Output Description

[[均值下限，均值上限],[方差比下限，方差比上限]]，均为浮点数
'''
log(Solution().solve())
