# https://www.hackerrank.com/challenges/s10-quartiles/problem

"""
Objective
In this challenge, we practice calculating quartiles. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, X, of n integers, calculate the respective first quartile (Q1), second quartile (Q2), and third quartile (Q3).
It is guaranteed that Q1, Q2, and Q3 are integers.
"""

# quartiles calculated acsording to the challenge and based on the first method described in the Wikipedia:
# https://en.wikipedia.org/wiki/Quartile#Method_1

# number of elements in list computed using len()
# following variable only need for the challenge to work but not for the script
n = input()

ls_val = list(map(int, input().rstrip().split()))
ls_val.sort()

# function to calculate the median
def med(ls_val):
    ln_ls_val = len(ls_val)
    mid = len(ls_val)//2
    return (ls_val[mid] + ls_val[-mid-1]) / 2

# function to split a list in two, if uneven upper half will contain the extra value
def split_list(ls_val):
    half = len(ls_val)//2
    return ls_val[:half], ls_val[half:]

# function to calculate Q1 and Q3
def Q1_Q3(ls_val, Q2):
    # if list len is uneven the med/Q2 is the mid number and not an average
    # if that is the case remove that number
    if len(ls_val)%2 == 1:
        ls_val.remove(Q2)
    ls_val_Q1, ls_val_Q3 = split_list(ls_val)
    return med(ls_val_Q1), med(ls_val_Q3)

Q2 = med(ls_val)
Q1, Q3 = Q1_Q3(ls_val, Q2)

print(int(Q1))
print(int(Q2))
print(int(Q3))
