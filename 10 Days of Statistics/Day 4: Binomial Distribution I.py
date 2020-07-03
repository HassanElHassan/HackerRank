# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem
from itertools import combinations
from math import factorial as fact

# function same result as len(list(combinations(range(n),x)))
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


ls_input = list(map(float, input().rstrip().split()))

# the terms of the ratio
# antecedent or first term
boys = ls_input[0]
# consequent or second term
girls = ls_input[1]

# the total number of trials
n = 6

# list of number of successes 
ls_x = [3,4,5,6]

# the probability of success of 1 trial
p = boys/(boys+girls)

# total probability for list of number of successes
total_prob_all = 0
for x in ls_x:
    total_prob_all += b(x, n, p)  

print(round(total_prob_all,3))
