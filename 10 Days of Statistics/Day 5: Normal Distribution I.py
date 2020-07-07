# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem

"""
Objective
In this challenge, we learn about normal distributions.

Task
In a certain plant, the time taken to assemble a car is a random variable, X, having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours.
What is the probability that a car can be assembled at this plant in:
*Less than 19.5 hours?
*Between 20 and 22 hours?
"""

from math import sqrt, erf

# function to calculate the Cumulative probability
def cum_prob(X_mean, X_sd, x):
    erf_parameter = (x - X_mean) / (X_sd * sqrt(2))
    return 0.5 * (1 + erf(erf_parameter))

# respective mean and standard deviation for X
X_mean, X_sd = map(float, input().strip().split())

# Q1, what is the probability that a car can be assembled at this plant in less than
Q1_time = float(input().strip())

# Q2, what is the probability that a car can be assembled at this plant Between
Q2_time_lower, Q2_time_upper = map(float, input().strip().split())

# Q1 probability
Q1_prob = cum_prob(X_mean, X_sd, Q1_time)

# Q2 probability lower 
Q2_prob_lower = cum_prob(X_mean, X_sd, Q2_time_lower)
# Q2 probability upper
Q2_prob_upper = cum_prob(X_mean, X_sd, Q2_time_upper)
# Q2 upper - lower to get the asked probability
Q2_prob = Q2_prob_upper - Q2_prob_lower

print(round(Q1_prob,3))
print(round(Q2_prob,3))
