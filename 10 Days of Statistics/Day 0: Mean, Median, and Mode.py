# challenge: https://www.hackerrank.com/challenges/s10-basic-statistics/problem
# all 3 stats and more can be computed using the statistics library

"""
Objective
In this challenge, we practice calculating the mean, median, and mode.

Task
Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines.
If your array contains more than one modal value, choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of 1 decimal place.
"""

from collections import Counter

def avg(ls_val):
    return round(sum(ls_val)/len(ls_val),1)

def med(ls_val):
    ln_ls_val = len(ls_val)
    mid = len(ls_val)//2
    return round((ls_val[mid] + ls_val[-mid-1]) / 2, 1)

def mod(ls_val):
    occ = Counter(ls_val)
    return occ.most_common(1)[0][0]

# number of elements in list computed using len()
# following variable only needed for the challenge to work but not for the script
n = input()

ls_val = list(map(int, input().rstrip().split()))
ls_val.sort()

print(avg(ls_val))
print(med(ls_val))
print(mod(ls_val))
