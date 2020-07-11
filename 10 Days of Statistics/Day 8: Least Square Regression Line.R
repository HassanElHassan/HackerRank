# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

# exercise can easily be solved using lm(y ~ x) that returns the slope and intercept

# built-in function cov() is for sample not population
# the build in sd() function is for sample not population
# an option -> sqrt((n-1)/n) * sd(x)

# function to calculate the Covariance, both lists should be of same length
# Σ( (xi-µx)*(yi-µy) ) / n
covariance <- function(X,Y){
    n <- length(X)
    X_min_mean <- X - mean(X)
    Y_min_mean <- Y - mean(Y)
    sum( (X_min_mean) * (Y_min_mean) ) / n 
}

# function to calculate the population sd
popsd <- function(v_val){
    # average the elements in the vector
    v_val_avg <- mean(v_val)
    # squared distance from the mean
    v_val_dist <- (v_val-v_val_avg)^2
    # average squared distance from the mean
    v_val_dist_avg <- sum(v_val_dist) / length(v_val)
    # SD by square root of average squared distance from the mean (variance)
    sqrt(v_val_dist_avg)
}   

# function to calculate the pearson correlation coefficient
# covariance / (σx*σy)
pcc <- function(X,Y){
    covariance(X,Y) / ( popsd(X) * popsd(Y) )
}

# calculate the slope using pcc, y=a+bx -> b is the slope
slope <- function(x,y){
    pcc(x,y) * ( popsd(y) / popsd(x) )
}

# calculate the intercept, y=a+bx -> a is the intercept
intercept <- function(x,y){
    mean(y) - slope(x,y) * mean(x)
}

# student's Math aptitude test score
x <- c(95,85,80,70,60)
# student's Statistics course grade
y <- c(85,95,70,65,70)

# y=a+bx
cat( round( ( intercept(x,y) + slope(x,y)*80 ) ,3 ) )

