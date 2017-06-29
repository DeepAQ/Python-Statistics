# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
import numpy as np

from log_api import log


class Solution():
    def solve(self, A):
        return np.poly1d(A) * np.poly1d(np.array([2.0, 0.0, -1.0, 1.0]))


'''
在Numpy中，多项式函数的系数可以用一维数组表示，例如对于f(x)=2x^3-x+1可表示为f=np.array([2.0,0.0,-1.0,1.0])，而np.poly1d()方法可以将多项式转换为poly1d(一元多项式)对象，返回多项式函数的值，请利用poly1d()方法计算多项式g(x)(例如g(x)=x^2+2x+1)和f(x)的乘积并将结果返回

Input / Output

Input Example

np.array([1.0, 2.0, 1.0])

Input Description

多项式g(x)的一维数组表示

Output Example

np.poly1d([2.0,4.0,1.0,-1.0,1.0,1.0])

Output Description

f(x)*g(x)的poly1d对象
'''
log(Solution().solve(np.array([1.0, 2.0, 1.0])))
