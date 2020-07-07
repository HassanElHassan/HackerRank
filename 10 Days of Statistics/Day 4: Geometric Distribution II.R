# https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem

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

# the inspection we want the probability of the first defect being discovered
# is also the total inspections(trials), first are non-defected last is defected
n <- as.numeric(dataset[3])
# so the number of successes is 1
x = 1

# sum the P that the 1st defect is found during the 1st, 2nd, 3rd, 4th and 5th inpsection
# the probability if n = 1 and it's defective = p
# remaining posibilities 2 to n
total_prob <- p + sum(sapply(seq(from = 2, to = n), FUN=prob, x=x, p=p))

cat(round(total_prob, digits=3))

close(con)
