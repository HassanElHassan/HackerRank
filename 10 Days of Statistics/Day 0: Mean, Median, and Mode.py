# challenge: https://www.hackerrank.com/challenges/s10-basic-statistics/problem
# all 3 stats and more can be computed using the statistics library

from collections import Counter

# number of elements in list computed using len()
# following variable only need ffor the challenge to work but not for the script
n = input()

ls_val = list(map(int, input().rstrip().split()))
ls_val.sort()

def avg(ls_val):
    return round(sum(ls_val)/len(ls_val),1)

def med(ls_val):
    ln_ls_val = len(ls_val)
    mid = len(ls_val)//2
    return round((ls_val[mid] + ls_val[-mid-1]) / 2, 1)

def mod(ls_val):
    occ = Counter(ls_val)
    return occ.most_common(1)[0][0]

print(avg(ls_val))
print(med(ls_val))
print(mod(ls_val))
