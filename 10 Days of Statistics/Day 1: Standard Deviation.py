# https://www.hackerrank.com/challenges/s10-standard-deviation/problem

"""
Objective
In this challenge, we practice calculating standard deviation.

Task
Given an array, X, of N integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of 1 decimal place.
An error margin of +-0.1 will be tolerated for the standard deviation.
"""

# challenge can easily be solved using statistics.pstdev()

import math

# function to calculate the mean/average
def avg(ls_val):
    return round(sum(ls_val)/len(ls_val),1)

# function to calculate the average squared distance from the mean, the Variance
def variance(ls_val):
    ls_val_avg = avg(ls_val)
    sum_sq_dist = 0
    for i in ls_val:
        # substract the avg from the i value and sum to the total squared distance
        sum_sq_dist +=(i-ls_val_avg)**2
    #devide the sum of the squared distances by the count of elements in the list
    return  sum_sq_dist/len(ls_val)
    
    
# number of elements in list computed using len()
# following variable only needed for the challenge to work but not for the script
n = input()

ls_val = list(map(float, input().strip().split()))

ls_val_var = variance(ls_val)

print(round(math.sqrt(ls_val_var),1))
