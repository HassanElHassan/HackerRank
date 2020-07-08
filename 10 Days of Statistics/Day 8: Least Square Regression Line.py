# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

# use of scipy/numpy not llowed

"""
Objective
In this challenge, we practice using linear regression techniques.

Task
A group of five students enrolls in Statistics immediately after taking a Math aptitude test. Each student's Math aptitude test score, x, and Statistics course grade, y:
x = [95,85,80,70,60]
y = [85,95,70,65,70]

If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics? Determine the equation of the best-fit line using the least squares method, then compute and print the value of y when x=80.
"""

from math import sqrt

# function to calculate the Covariance, both lists should be of same length
# Σ( (xi-µx)*(yi-µy) ) / n
def covariance(X,Y):
    n = len(X)
    X_mean = sum(X)/n
    Y_mean = sum(Y)/n
    return ( sum( [ ( (x-X_mean) * (y-Y_mean) ) for x, y in zip(X, Y) ] ) / n )

# function to calculate the average squared distance from the mean, the Variance
def variance(ls_val):
    n = len(ls_val)
    ls_val_avg = sum(ls_val)/n
    sum_sq_dist = 0
    for i in ls_val:
        # substract the avg from the i value and sum to the total squared distance
        sum_sq_dist +=(i-ls_val_avg)**2
    #devide the sum of the squared distances by the count of elements in the list
    return  sum_sq_dist/len(ls_val)

# function to calculate the standard deviation using the variance
def sd(ls_val):
    return sqrt(variance(ls_val))

# function to calculate the pearson correlation coefficient
# covariance / (σx*σy)
def pcc(X,Y):
    return covariance(X,Y) / ( sd(X) * sd(Y) )

# calculate the slope using pcc, y=a+bx -> b is the slope
def slope(x,y):
    return pcc(x,y) * ( sd(y) / sd(x) )

# calculate the intercept, y=a+bx -> a is the intercept
def intercept(x,y):
    n = len(x)
    x_mean = sum(x)/n
    y_mean = sum(y)/n
    return y_mean - slope(x,y) * x_mean

# student's Math aptitude test score
x = [95,85,80,70,60]
# student's Statistics course grade
y = [85,95,70,65,70]

# y=a+bx
print( round( ( intercept(x,y) + slope(x,y)*80 ) ,3 ) )
