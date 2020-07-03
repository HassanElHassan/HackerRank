# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

# the excersise can easily be solved using sum(dbinom(ls_x, size=n, prob=p))

# the following function generated the same result as ncol(combn(6,3))
# combinations 
comb <- function(n, x){
    factorial(n) / (factorial(x) * factorial(n-x))
}   

# function to calculate the probability of an event
prob <- function(p, x, n){
    # The probability of failure of 1 trial 
    q <- 1 - p
    # The number of failures 
    y <- n - x

    (p**x)*(q**y)
}

# function to calculate the total probability of 1 number of successes
b <- function(x, n, p){
    # events with x
    events <- comb(n, x)
    # probability for each
    prob_each <- prob(p, x, n)
    # total probability 
    events * prob_each
}

con <- file("stdin", open = "r")

dataset <- unlist(strsplit(readLines(con), split="\\s"))

# antecedent or first term
boys <- as.numeric(dataset[1])

# consequent or second term
girls <- as.numeric(dataset[2])

# the total number of trials
n <- 6

# vector of number of successes 
ls_x <- c(3,4,5,6)

# the probability of success of 1 trial
p <- boys/(boys+girls)

# total probability for list of number of successes
total_prob_all <- sum(sapply(ls_x, FUN=b, n=n, p=p))

cat(round(total_prob_all, digits=3))

close(con)
