# https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem

# function to calculate the value of Spearman's rank correlation coefficient
# for data sets that contain unique values and of same length
srcc <- function(X,Y){
    # length of data set
    n = length(X)
    # rank of X
    X_rank = rank(X)
    # rank of Y
    Y_rank = rank(Y)
    # the sum of the squared difference between ranks of each pair
    sum_d_sq = sum( (X_rank - Y_rank)^2 )
    
    1- ( (6*sum_d_sq) / (n*(n**2-1)) )
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

cat(round(srcc(X,Y),digits=3))

close(con)
