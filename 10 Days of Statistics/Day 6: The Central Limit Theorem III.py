# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem

"""
Objective
In this challenge, we practice solving problems based on the Central Limit Theorem.

Task
You have a sample of 100 values from a population with mean µ=500 and with standard deviation σ=80.
Compute the interval that covers the middle 95% of the distribution of the sample mean; in other words, compute A and B such that P(A<x<B)=0.95. Use the value of a=1.96.
Note that z is the z-score.
"""

from math import sqrt

# sample size
n = float(input().strip())

# population mean 
X_mean_pop = float(input().strip())

# population standard deviation
X_sd_pop = float(input().strip())

# the distribution percentage we want to cover (as a decimal)
dist_perc = float(input().strip())

# the value of z
z = float(input().strip())

# expected sample mean = population mean
X_mean_samp = X_mean_pop

# sample standard deviation 
X_sd_samp = X_sd_pop / sqrt(n)

# P(A<x<B)=0.95, z=z, is (-zσ) - mean - (+zσ) e.g. z=1.96 -> (-1.96σ) - mean - (+1.96σ)
# z = ( x - µ ) / σ  -> x = ( z * σ) + µ
# lower value
A = ( -z * X_sd_samp) + X_mean_samp
# upper values
B = ( z * X_sd_samp) + X_mean_samp

print(round(A,2))
print(round(B,2))
