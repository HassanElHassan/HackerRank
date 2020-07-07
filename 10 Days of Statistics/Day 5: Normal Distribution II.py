# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

"""
Objective
In this challenge, we go further with normal distributions.

Task
The final grades for a Physics exam taken by a large group of students have a mean of µ=70 and a standard deviation of σ=10.
If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:
1. Scored higher than 80 (i.e., have a grade > 80)?
2. Passed the test (i.e., have a grade >= 60)?
3. Failed the test (i.e., have a grade < 60)?
Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.
"""

from math import sqrt, erf

# function to calculate the Cumulative probability
def cum_prob(X_mean, X_sd, x):
    erf_parameter = (x - X_mean) / (X_sd * sqrt(2))
    return 0.5 * (1 + erf(erf_parameter))

# respective mean and standard deviation for X
X_mean, X_sd = map(float, input().strip().split())

# Q1, Scored higher than
Q1_score = float(input().strip())

# Q2 and Q3 pass/fail threshold
Q2Q3_threshold = float(input().strip())

# Q1 probability higher than Q1_score in  %
# the function calculates the left area, the total area is 1, right area = 1 - left area
Q1_prob = ( 1 - cum_prob(X_mean, X_sd, Q1_score) ) * 100

# Q2 probability passed >= Q2Q3_threshold in  %
# the function calculates the left area, the toal area is 1, right area = 1 - left area
Q2_prob = ( 1 - cum_prob(X_mean, X_sd, Q2Q3_threshold) ) * 100

# Q3 probability failed < Q2Q3_threshold in  %
Q3_prob = cum_prob(X_mean, X_sd, Q2Q3_threshold) * 100


print(round(Q1_prob,2))
print(round(Q2_prob,2))
print(round(Q3_prob,2))
