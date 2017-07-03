# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
import numpy as np
from scipy.stats import t

from log_api import log


class Solution():
    def solve(self):
        temp_2010 = [25.7, 25.6, 25.6, 22.4, 21.7, 23.3, 23, 22.2, 27.9, 27.2, 28.4, 27.5, 29.3, 29.4, 25.1, 26, 29.1,
                     29.4, 29.9, 28.8, 28.1, 28.4, 25, 23.6, 20.6, 16.4, 24.7, 18.3, 15.4, 21.3, 22.9]
        temp_2014 = [27.3, 27.7, 27.9, 23.6, 20.6, 24.3, 22.6, 22.5, 31, 30.8, 31.3, 31.1, 29.6, 31.6, 28.6, 30.1, 30.6,
                     32, 27.5, 27.7, 27.9, 30.5, 26.5, 23.1, 19.9, 15.9, 28.3, 21, 18.2, 24.4, 22.8]
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
