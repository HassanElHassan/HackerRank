# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem

# erf(z) can be calculated using (2 * pnorm(x * sqrt(2)) - 1)

con <- file("stdin", open = "r")

dataset <- unlist(strsplit(readLines(con), split="\\s"))

# mean for X
X_mean <- as.numeric(dataset[1])
# standard deviation for X
X_sd  <- as.numeric(dataset[2])

# Q1, what is the probability that a car can be assembled at this plant in less than
Q1_time   <- as.numeric(dataset[3])

# Q2, what is the probability that a car can be assembled at this plant
#Between
Q2_time_lower <- as.numeric(dataset[4])
# and
Q2_time_upper <- as.numeric(dataset[5])

# Q1 probability
Q1_prob <- pnorm(Q1_time, mean = X_mean, sd = X_sd)

# Q2 probability lower 
Q2_prob_lower <- pnorm(Q2_time_lower, mean = X_mean, sd = X_sd)
# Q2 probability upper
Q2_prob_upper <- pnorm(Q2_time_upper, mean = X_mean, sd = X_sd)
# Q2 upper - lower to get the asked probability
Q2_prob <- Q2_prob_upper - Q2_prob_lower

cat(round(Q1_prob, digits=3))
cat("\n")
cat(round(Q2_prob, digits=3))

close(con)

