# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

"""
Objective
In this challenge, we go further with binomial distributions.

Task
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized.
What is the probability that a batch of 10 pistons will contain:
1. No more than 2 rejects?
2. At least 2 rejects?
"""

# from itertools import combinations
from math import factorial as fact

# the following function generates the same result as len(list(combinations(range(n),x)))
# combinations 
def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

# function to calculate the probability of an event
def prob(p, x, n):
    # The probability of failure of 1 trial 
    q = 1 - p
    # The number of failures 
    y = n - x

    return (p**x)*(q**y) 

# function to calculate the total probability of 1 number of successes
def b(x, n, p):
    # events with x
    events = comb(n, x)
    # probability for each
    prob_each = prob(p, x, n)
    # total probability 
    return events * prob_each

# x, y = map(float, input().strip().split()) also an option
ls_input = list(map(float, input().strip().split()))

# the probability of success of 1 trial
p = ls_input[0] / 100

# the total number of trials
n = ls_input[1]

# 10 pistons will contain no more than 2 rejects.
# list of number of successes 
ls_x = [0,1,2]
# total probability for list of number of successes
total_prob_all = 0
for x in ls_x:
    total_prob_all += b(x, n, p)  

# 10 pistons will contain at least 2 rejects.
# an option -> 1-P[0,1] 
# list of number of successes 
ls_x2 = [2,3,4,5,6,7,8,9,10]
# total probability for list of number of successes
total_prob_all2 = 0
for x in ls_x2:
    total_prob_all2 += b(x, n, p)  

print(round(total_prob_all,3))
print(round(total_prob_all2,3))
