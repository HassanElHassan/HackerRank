# https://www.hackerrank.com/challenges/s10-multiple-linear-regression/problem

"""
Objective
In this challenge, we practice using multiple linear regression.

Task
Andrea has a simple equation (=1 feature set):
Y = a+b1f1+b2f2+...+bmfm
for (m+1) real constants (a, f1, f2, ..., fm). We can say that the value of Y depends on m features. Andrea studies this equation for n different feature sets (f1, f2, ..., fm) and records each respective value of Y. If she has q new feature sets, can you help Andrea find the value of Y for each of the sets?
Note: You are not expected to account for bias and variance trade-offs.

Output Format
For each of the q feature sets, print the value of Y on a new line (i.e., you must print a total of q lines).

Explanation
We're given m=2, so Y=a+b1f1+b2f2. We're also given n=7, so we determine that Andrea studied n feature sets:
We use the information above to find the values of a, b1, and b2. Then, we find the value of Y for each of the q feature sets.
"""
# the following can be used to compute B (intercept(a) and the slopes(b))
"""
from sklearn import linear_model
lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_
print (a, b)
"""

import numpy as np
from numpy.linalg import inv

# number of observed features (m) and  number of feature sets studied (n), str to int
m, n = map(int, input().strip().split(' '))

# Each of the n subsequent input lines contain m+1 space-separated decimals
# the first m elements are features (f1,f2,..), and the last element is the value of Y for the line's feature set.
# variable to store the features from each feature set, list per feature set
X = []
# variable to store Y from each feature set, list per y from each feature set
Y = []
# loop over lines/feature sets
for i in range(n):
    # input of each line, the line's feature set, string to float later by numpy
    data = input().strip().split(' ')
    # append 1 for a + the first m elements, the features (f1,f2,..) of current feature set
    X.append([1]+data[:m])
    # append the last element, the value of Y for current feature set
    Y.append(data[m:])
# transform to array
X = np.array(X,float)
Y = np.array(Y,float)

# number of feature sets Andrea wants to query for, str to int
q = int(input().strip())

# Each of q contains m space-separated decimals describing the feature sets
X_query = []
for i in range(q):
    # string to float later by numpy
    X_query.append([1] + input().strip().split(' '))
# transform to array
X_query = np.array(X_query,float)

# find the Matrix B, .T to transpose and @ for matrix multiplication
# Y = X*B  ->  X.T*Y = X.T*X*B  ->  B = inv(X.T*X)*X.T*Y
B = inv(X.T@X)@X.T@Y

# find the value of Y for each of the q feature sets
Y_query = X_query@B

# print per line Y of each feature set
for Y in Y_query:
    print(round(float(Y),2))
