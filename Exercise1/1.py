# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
from log_api import log


class Solution():
    def solve(self, A):
        result = {}
        for i in range(0, 10):
            result[i] = 0
        for str in A:
            for c in str:
                i = int(c)
                result[i] += 1
        return result


'''
已知有一个由数字字符串构成的列表，统计列表中数字字符'0'-'9'各自出现的次数并返回统计结果

Input / Output

Input Example

['12','34','567', '36','809','120']

Input Description

一个由数字字符串构成的列表

Output Example

{0:2, 1:2, 2:2, 3:2, 4:1, 5:1, 6:2, 7:1, 8:1, 9:1}

Output Description

各数字字符的出现次数
'''
log(Solution().solve(['12', '34', '567', '36', '809', '120']))
