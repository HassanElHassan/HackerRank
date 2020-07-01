# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

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

ls_elem = list(map(float, input().rstrip().split()))
ls_freq = list(map(int, input().rstrip().split()))

ls_values = elem_x_freq(ls_elem,ls_freq)
ls_values.sort()

Q2 = st.median(ls_values)
Q1, Q3 = Q1_Q3(ls_values, Q2)

print(Q3-Q1)
