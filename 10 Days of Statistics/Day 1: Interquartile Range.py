# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

"""
Objective
In this challenge, we practice calculating the interquartile range.

Task
The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3-Q1).
Given an array, X, of n integers and an array, F, representing the respective frequencies of X's elements, construct a data set, S, where each xi occurs at frequency fi.
Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place.

Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.
"""

# quartiles calculated based on the first method described in the Wikipedia:
# https://en.wikipedia.org/wiki/Quartile#Method_1

# numpy not allowed for this challenge so np.repeat() not an option
# import numpy as np gives ModuleNotFoundError: No module named 'numpy'

import statistics as st

# function to create the value list by multiplying the elements by their frequencies
def elem_x_freq(ls_elem,ls_freq):
    len_ls = len(ls_elem)
    ls_values = []
    for i in range(len_ls):
        ls_values += [ls_elem[i]]*ls_freq[i]
    return ls_values

# function to split a list into two, if uneven upper half will contain the extra value
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
    return st.median(ls_val_Q1), st.median(ls_val_Q3)

# number of elements in list computed using len()
# following variable only needed for the challenge to work but not for the script
n = input()

ls_elem = list(map(float, input().strip().split()))
ls_freq = list(map(int, input().strip().split()))

ls_values = elem_x_freq(ls_elem,ls_freq)
ls_values.sort()

Q2 = st.median(ls_values)
Q1, Q3 = Q1_Q3(ls_values, Q2)

print(Q3-Q1)
