# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
from log_api import log


class Solution():
    def solve(self, A):
        result = {}
        for str in A:
            result[str] = result.get(str, 0) + 1
        return result


'''
已知列表fruits中顺序保存了某商店每日出售的水果品名，例如fruits=['apple','banana','cherry','pineapple','banana','peach','pear','peach','cherry' ]，完成函数solve()计算每一种水果的出售次数，存入字典result中并将结果返回

Input / Output

Input Example

['apple', 'banana', 'cherry', 'pineapple', 'banana', 'peach', 'pear','peach', 'cherry' ]

Input Description

一个纪录了水果出售纪录的列表

Output Example

{'pear':1, 'banana':2, 'cherry':2, 'peach':2, 'pineapple':1, 'apple':1}

Output Description

水果出售次数统计结果
'''
log(Solution().solve(['apple', 'banana', 'cherry', 'pineapple', 'banana', 'peach', 'pear', 'peach', 'cherry']))
