# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

"""
Objective
In this challenge, we learn about Poisson distributions.
Task
A random variable, X, follows Poisson distribution with mean of 2.5. Find the probability with which the random variable X is equal to 5.
"""

from math import exp, factorial

# function to calculate the probability based on the poisson distribution
def poisson(A,k):
    return ( (A**k) * (exp(-A)) ) / factorial(k)

# contains X's mean
A = float(input().strip())
# contains the value we want the probability for
k = float(input().strip())

print(poisson(A,k))
