# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

# erf(z) can be calculated using (2 * pnorm(x * sqrt(2)) - 1)

con <- file("stdin", open = "r")

dataset <- unlist(strsplit(readLines(con), split="\\s"))

# mean for X
X_mean <- as.numeric(dataset[1])
# standard deviation for X
X_sd  <- as.numeric(dataset[2])

# Q1, Scored higher than
Q1_score <- as.numeric(dataset[3])

# Q2 and Q3 pass/fail threshold
Q2Q3_threshold <- as.numeric(dataset[4])

# Q1 probability higher than Q1_score in  %
# the function calculates the left area, the total area is 1, right area = 1 - left area
Q1_prob <- ( 1 - pnorm(Q1_score, mean = X_mean, sd = X_sd) ) * 100

# Q2 probability passed >= Q2Q3_threshold in  %
# the function calculates the left area, the toal area is 1, right area = 1 - left area
Q2_prob <- ( 1 - pnorm(Q2Q3_threshold, mean = X_mean, sd = X_sd) ) * 100

# Q3 probability failed < Q2Q3_threshold in  %
Q3_prob <- pnorm(Q2Q3_threshold, mean = X_mean, sd = X_sd) * 100

cat(round(Q1_prob, digits=2))
cat("\n")
cat(round(Q2_prob, digits=2))
cat("\n")
cat(round(Q3_prob, digits=2))

close(con)
