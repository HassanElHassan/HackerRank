# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

# the excersise can easily be solved using dgeom(n-1, prob = 1/3)
  
# function to calculate the probability of an event
# for Geometric Distribution:
# number of successes (x) will be 1 so number of failures will be n-1 -> p*(q**n-1)
prob <- function(p, x, n){
    # The probability of failure of 1 trial 
    q <- 1 - p
    # The number of failures 
    y <- n - x

    (p**x)*(q**y)
}

con <- file("stdin", open = "r")

# the respective space-separated numerator and denominator for the probability of a defect
dataset <- unlist(strsplit(readLines(con), split="\\s"))
numerator  <- as.numeric(dataset[1])
denominator <- as.numeric(dataset[2])
# The probability that a machine produces a defective product (a success)
p <- numerator/denominator

# the inspection we want the probability of being the first defect for (first success)
# is also the total inspections(trials), first are non-defected last is defected
n <- as.numeric(dataset[3])
# so the number of successes is 1
x = 1

cat(round(prob(p,x,n), digits=3))

close(con)
