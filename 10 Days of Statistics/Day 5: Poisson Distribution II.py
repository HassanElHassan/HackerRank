# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

"""
Objective
In this challenge, we go further with Poisson distributions. 

Task
The manager of a industrial plant is planning to buy a machine of either type  or type . For each day’s operation:

* The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating A is C(A)=160+40*X**2.
* The number of repairs, Y, that machine  needs is a Poisson random variable with mean 1.55. The daily cost of operating B is C(B)=128+40*Y**2.

Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.
"""

# x, y = map(float, input().strip().split()) also an option
ls_input = list(map(float, input().strip().split()))

# mean of A
A = ls_input[0]
# mean of B
B = ls_input[1]

# expected daily cost of machine A using E[X**2] = lambda + lambda**2
A_cost = 160 + 40 * (A + A**2)
# expected daily cost of machine B using E[X**2] = lambda + lambda**2
B_cost = 128 + 40 * (B + B**2)

print(round(A_cost,3))
print(round(B_cost,3))
