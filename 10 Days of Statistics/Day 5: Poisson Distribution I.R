# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

# function to calculate the probability based on the poisson distribution
poisson <- function(A,k){
    ( (A**k) * (exp(-A)) ) / factorial(k)
}

con <- file("stdin", open = "r")

dataset <- unlist(strsplit(readLines(con), split="\\s"))

# contains X's mean
A <- as.numeric(dataset[1])

# contains the value we want the probability for
k <- as.numeric(dataset[2])

cat(round(poisson(A,k), digits=3))

close(con)
