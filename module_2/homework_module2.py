import math
from sympy import *


def func_sum_e(n: Number):
    sum = 0
    for num in range(1, n + 1):
        sum += math.log(num, math.e)
    return sum


def func_e_extent_multiplication(n: Number):
    sum = 1
    for num in range(1, n + 1):
        sum *= num
        expression = 15 * sqrt(4)
    return math.log(sum, math.e)


expression_1 = func_sum_e(n=4)
expression_2 = func_e_extent_multiplication(n=4)
print()


