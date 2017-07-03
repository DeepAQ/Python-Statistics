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
        url_2010 = 'http://py.mooctest.net:8081/dataset/temperature/temperature_2010.csv'
        url_2014 = 'http://py.mooctest.net:8081/dataset/temperature/temperature_2014.csv'
        temp_2010 = list(pd.read_csv(urlopen(url_2010), encoding='gbk', skiprows=range(0, 6) + range(37, 40), header=None)[8])
        temp_2014 = list(pd.read_csv(urlopen(url_2014), encoding='gbk', skiprows=range(0, 5) + range(36, 39), header=None)[8])
        n = len(temp_2014)
        diff = [temp_2014[i] - temp_2010[i] for i in range(0, n)]
        # H_0: u_d <= 0, H_1: u_d > 0
        mean = np.mean(diff)
        sd = np.std(diff)
        tt = mean / sd * np.sqrt(n)
        if tt > t.ppf(0.95, n - 1):
            return 'YES'
        else:
            return 'NO'


'''
当前世界全球变暖现象严重，为了探索中国是否也存在这个现象，现调查了中国主要城市的全年气温情况，包括2010年全年气温状况与2014年全年气温状况，以8月份气温为例，假设主要城市温度符合正态分布，试比较是否存在温度上升现象？（需给出证明过程，仅回答YES或NO不得分）

Output Example

'YES'

Output Description

如果存在气温上升现象，返回'YES'否则返回'NO'
'''
log(Solution().solve())
