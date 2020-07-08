# https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem

# use of scipy/numpy not llowed

"""
Objective
In this challenge, we practice calculating the Pearson correlation coefficient.

Task
Given two n-element data sets, X and Y, calculate the value of the Pearson correlation coefficient.
"""

from math import sqrt

# function to calculate the Covariance, both lists should be of same length
# Σ( (xi-µx)*(yi-µy) ) / n
def covariance(X,Y):
    n = len(X)
    X_mean = sum(X)/n
    Y_mean = sum(Y)/n
    return ( sum( [ ( (x-X_mean) * (y-Y_mean) ) for x, y in zip(X, Y) ] ) / n )

# function to calculate the average squared distance from the mean, the Variance
def variance(ls_val):
    n = len(ls_val)
    ls_val_avg = sum(ls_val)/n
    sum_sq_dist = 0
    for i in ls_val:
        # substract the avg from the i value and sum to the total squared distance
        sum_sq_dist +=(i-ls_val_avg)**2
    #devide the sum of the squared distances by the count of elements in the list
    return  sum_sq_dist/len(ls_val)

# function to calculate the standard deviation using the variance
def sd(ls_val):
    return sqrt(variance(ls_val))

# function to calculate the pearson correlation coefficient
# covariance / (σx*σy)
def pcc(X,Y):
    return covariance(X,Y) / ( sd(X) * sd(Y) )

# size of data sets X and Y
# number of elements computed using len()
# following variable only needed for the challenge to work but not for the script
n = float(input().strip())

# data set X
X = list(map(float, input().strip().split()))

# data set Y
Y = list(map(float, input().strip().split()))

print(round(pcc(X,Y),3))
