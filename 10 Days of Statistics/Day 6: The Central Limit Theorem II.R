# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem

# erf(z) can be calculated using (2 * pnorm(x * sqrt(2)) - 1)

con <- file("stdin", open = "r")

dataset <- unlist(strsplit(readLines(con), split="\\s"))

# number of last-minute tickets available
tickets <- as.numeric(dataset[1])

# number of students waiting to buy tickets
n <- as.numeric(dataset[2])

# mean number of purchased tickets
X_mean <- as.numeric(dataset[3])

# standard deviation of the mean number of purchased tickets
X_sd <- as.numeric(dataset[4])

# sum mean number of all students, µ'=nxµ
X_mean_sum <- n * X_mean

# standard deviation of the sum mean number of all students, σ'=sqrt(n)xσ 
X_sd_sum <- sqrt(n) * X_sd

# probability that all students can successfully purchase the remaining tickets 
p <- pnorm(tickets, mean = X_mean_sum, sd = X_sd_sum)

cat(round(p, digits=4))

close(con)
