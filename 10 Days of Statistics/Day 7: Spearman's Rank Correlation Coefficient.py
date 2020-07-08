# https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem

# use of scipy/numpy not llowed

"""
Objective
In this challenge, we practice calculating Spearman's rank correlation coefficient.

Task
Given two n-element data sets, X and Y, calculate the value of Spearman's rank correlation coefficient.
"""

# function to calculate the value of Spearman's rank correlation coefficient
# for data sets that contain unique values and of same length
def srcc(X,Y):
    # length of data set
    n = len(X)
    # rank of X
    X_rank = [sorted(X).index(x) + 1 for x in X]
    # rank of Y
    Y_rank = [sorted(Y).index(x) + 1 for x in Y]
    # the sum of the squared difference between ranks of each pair
    sum_d_sq = sum( [ ( (x - y)**2 ) for x, y in zip(X_rank,Y_rank) ] )
    
    return 1- ( (6*sum_d_sq) / (n*(n**2-1)) )

# size of data sets X and Y
# following variable only needed for the challenge to work, number of elements computed using len()
n = float(input().strip())

# data set X
X = list(map(float, input().strip().split()))

# data set Y
Y = list(map(float, input().strip().split()))

print(round(srcc(X,Y),3))
