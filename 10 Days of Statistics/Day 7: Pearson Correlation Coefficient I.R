# https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem

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

con <- file("stdin", open = "r")

dataset <- readLines(con)

# size of data sets X and Y
# following variable not used, number of elements computed using length 
n <- as.numeric(dataset[1])

# data set X
X <- unlist(strsplit(dataset[2], split=" "))
X <- as.numeric(X)

# data set Y
Y <- unlist(strsplit(dataset[3], split=" "))
Y <- as.numeric(Y)

cat(round(pcc(X,Y),digits=3))
