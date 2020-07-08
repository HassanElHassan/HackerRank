# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem
"""
Objective
In this challenge, we practice solving problems based on the Central Limit Theorem. 

Task
A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator.
The box weight of this type of cargo follows a distribution with a mean of µ=205 pounds and a standard deviation of σ=15 pounds.
Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?
"""

from math import sqrt, erf

# function to calculate the Cumulative probability
def cum_prob(X_mean, X_sd, x):
    erf_parameter = (x - X_mean) / (X_sd * sqrt(2))
    return 0.5 * (1 + erf(erf_parameter))

# maximum weight the elevator can transport
weight = float(input().strip())

# number of boxes in the cargo
n = float(input().strip())

# the mean weight of a cargo box
X_mean = float(input().strip())

# the standard deviation of the mean weight of a cargo box
X_sd = float(input().strip())

# the sum mean weight of all cargo boxes, µ'=nxµ
X_mean_sum = n * X_mean

# the standard deviation of the sum mean weight of all cargo boxes, σ'=sqrt(n)xσ 
X_sd_sum = sqrt(n) * X_sd

# probability that the elevator can successfully transport all boxes
p = cum_prob(X_mean_sum, X_sd_sum, weight)

print(round(p,4))
