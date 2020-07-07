# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

"""
Objective
In this challenge, we learn about geometric distributions.

Task
The probability that a machine produces a defective product is 1/3. What is the probability that the  defect is found during the 1st inspection?
"""

# function to calculate the probability of an event
# for Geometric Distribution:
# number of successes (x) will be 1 so number of failures will be n-1 -> p*(q**n-1)
def prob(p, x, n):
    # The probability of failure of 1 trial 
    q = 1 - p
    # The number of failures 
    y = n - x
    return (p**x)*(q**y) 

# the respective space-separated numerator and denominator for the probability of a defect
# x, y = map(float, input().strip().split()) also an option
ls_input = list(map(float, input().strip().split()))
numerator = ls_input[0]
denominator = ls_input[1]
# The probability that a machine produces a defective product (a success)
p = numerator/denominator

# the inspection we want the probability of being the first defect for (first success)
# is also the total inspections(trials), first are non-defected last is defected
n = int(input().strip())
# so the number of successes is 1
x = 1

print(round(prob(p,x,n),3))
