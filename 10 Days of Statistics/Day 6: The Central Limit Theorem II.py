# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem

"""
Objective
In this challenge, we practice solving problems based on the Central Limit Theorem.

Task
The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of µ=2.4 and a standard deviation of σ=2.0.
A few hours before the game starts, 100 eager students line up to purchase last-minute tickets.
If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?
"""

from math import sqrt, erf

# function to calculate the Cumulative probability
def cum_prob(X_mean, X_sd, x):
    erf_parameter = (x - X_mean) / (X_sd * sqrt(2))
    return 0.5 * (1 + erf(erf_parameter))

# number of last-minute tickets available
tickets = float(input().strip())

# number of students waiting to buy tickets
n = float(input().strip())

# mean number of purchased tickets
X_mean = float(input().strip())

# standard deviation of the mean number of purchased tickets
X_sd = float(input().strip())

# sum mean number of all students, µ'=nxµ
X_mean_sum = n * X_mean

# standard deviation of the sum mean number of all students, σ'=sqrt(n)xσ 
X_sd_sum = sqrt(n) * X_sd

# probability that all students can successfully purchase the remaining tickets 
p = cum_prob(X_mean_sum, X_sd_sum, tickets)

print(round(p,4))
