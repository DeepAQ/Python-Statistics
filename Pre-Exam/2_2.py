# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
from urllib2 import urlopen

import numpy as np
import pandas as pd
from scipy.stats import chi2, t

from log_api import log


class Solution():
    def solve(self):
        url_old = 'http://py.mooctest.net:8081/dataset/population/population_old.csv'
        url_total = 'http://py.mooctest.net:8081/dataset/population/population_total.csv'
        old_people = list(pd.read_csv(urlopen(url_old), encoding='gbk', skiprows=range(0, 3), header=None)[1])
        total_people = list(pd.read_csv(urlopen(url_total), encoding='gbk', skiprows=range(0, 5), header=None)[4])
        n = len(total_people)
        old_rate = [old_people[i] * 100.0 / total_people[i] for i in range(0, n)]
        mean = np.mean(old_rate)
        sd = np.std(old_rate)
        mean_delta = sd / np.sqrt(n) * t.ppf(0.95, n - 1)
        sqd_lower = (n - 1) * (sd ** 2) / chi2.ppf(1 - 0.05, n - 1)
        sqd_upper = (n - 1) * (sd ** 2) / chi2.ppf(0.05, n - 1)
        return [[mean - mean_delta, mean + mean_delta], [sqd_lower, sqd_upper]]


'''
人口普查是一项重要的国情调查，对于国家管理、制定各项方针政策具有重要的意义，中国最早的一次人口普查在西汉汉平帝元始二年进行，而自中华人民共和国建国以来分别在1953、1964、1982、1990、2000和2010年进行了共六次人口普查，其中第六次人口普查分别涉及到了人口增长、家庭户人口、性别构成、年龄构成、民族构成、受教育程度、城乡人口、人口流动性等八方面。现有《各地区分性别、健康状况的60岁及以上老年人口》调查数据、《各地区户数、人口数和性别比》调查数据，定义老龄率=60岁及以上人口数*100/总人口数，以北京市为例，其老龄率为250084*100/1849475=13.52，请编写python代码回答如下问题：

以各省市数据为代表，求取中国省级老龄率均值的置信区间、方差的置信区间，置信水平均为90%，假设老龄率符合正态分布

Output Example

[[mean_lower, mean_upper], [variance_lower, variance_upper]]

Output Description

[[均值下限，均值上限],[方差下限，方差上限]]，均为浮点数
'''
log(Solution().solve())
