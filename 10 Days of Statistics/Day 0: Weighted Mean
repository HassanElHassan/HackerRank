# challenge: https://www.hackerrank.com/challenges/s10-weighted-mean/problem
# numpy not allowed for this challenge
# import numpy as np gives ModuleNotFoundError: No module named 'numpy'

# number of elements in list computed using len()
# following variable only need for the challenge to work but not for the script
n=input()

ls_grade = list(map(int, input().rstrip().split()))

ls_weight = list(map(int, input().rstrip().split()))

# the following is based on numpy that cannot be used
"""
def weighted_mean(ls_grade, ls_weight):
    mult = np.multiply(ls_grade, ls_weight)
    mult_sum = mult.sum()
    weight_sum = sum(ls_weight)
    print(mult)
    print(mult_sum)
    print(weight_sum)
    return round(mult_sum/weight_sum,1)

weighted_mean(ls_grade, ls_weight)
"""

def weighted_mean(ls_grade, ls_weight):
    mult = [a * b for a, b in zip(ls_weight, ls_grade)]
    mult_sum = sum(mult)
    weight_sum = sum(ls_weight)
    return round(mult_sum/weight_sum,1)

print(weighted_mean(ls_grade, ls_weight))
