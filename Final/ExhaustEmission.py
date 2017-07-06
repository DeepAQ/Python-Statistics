# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
from urllib2 import urlopen

import numpy as np
import pandas as pd
from scipy.stats import t

from log_api import log


class Solution():
    def solve(self):
        url_2010 = 'http://py.mooctest.net:8081/dataset/air/exhaust_emission_2010.csv'
        url_2014 = 'http://py.mooctest.net:8081/dataset/air/exhaust_emission_2014.csv'
        data_2010 = list(pd.read_csv(urlopen(url_2010), encoding='gbk', skiprows=range(0, 9), header=None)[5].dropna() * 10000)
        data_2014 = list(pd.read_csv(urlopen(url_2014), encoding='gbk', skiprows=range(0, 6), header=None)[1].dropna())
        n = len(data_2014)
        diff = [data_2014[i] - data_2010[i] for i in range(0, n)]
        # H_0: u_d <= 0, H_1: u_d > 0
        mean = np.mean(diff)
        sd = np.std(diff, ddof=1)
        tt = mean / sd * np.sqrt(n)
        return [tt, 'YES' if tt > t.ppf(0.95, n - 1) else 'NO']


'''
为了探索中国气体污染物废气情况，现调查了主要城市的废气中主要污染物排放情况，包括2010年主要城市废气中主要污染物排放情况以及2014年主要城市废气中主要污染物排放情况，以工业二氧化硫排放量为例，试比较是否排放量变高的现象，并给出检验统计量的值，alpha=0.05,使用配对数据检验方法

Output Example

[value, conclusion]

Output Description

value为检验统计量的值，浮点数；如果存在排放量变高的现象，则conclusion为'YES'否则为'NO'
'''
log(Solution().solve())
