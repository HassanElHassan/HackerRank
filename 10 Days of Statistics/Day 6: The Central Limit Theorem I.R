# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem

# erf(z) can be calculated using (2 * pnorm(x * sqrt(2)) - 1)

con <- file("stdin", open = "r")

dataset <- unlist(strsplit(readLines(con), split="\\s"))

# maximum weight the elevator can transport
weight <- as.numeric(dataset[1])

# number of boxes in the cargo
n <- as.numeric(dataset[2])

# the mean weight of a cargo box
X_mean <- as.numeric(dataset[3])

# the standard deviation of the mean weight of a cargo box
X_sd <- as.numeric(dataset[4])

# the sum mean weight of all cargo boxes, µ'=nxµ
X_mean_sum <- n * X_mean

# the standard deviation of the sum mean weight of all cargo boxes, σ'=sqrt(n)xσ 
X_sd_sum <- sqrt(n) * X_sd

# probability that the elevator can successfully transport all boxes
p <- pnorm(weight, mean = X_mean_sum, sd = X_sd_sum)

cat(round(p, digits=4))

close(con)
