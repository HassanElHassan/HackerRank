# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem


con <- file("stdin", open = "r")

dataset <- unlist(strsplit(readLines(con), split="\\s"))

# sample size
n <- as.numeric(dataset[1])

# population mean 
X_mean_pop <- as.numeric(dataset[2])

# population standard deviation
X_sd_pop <- as.numeric(dataset[3])

# the distribution percentage we want to cover (as a decimal)
dist_perc <- as.numeric(dataset[4])

# the value of z
z <- as.numeric(dataset[5])

# expected sample mean = population mean
X_mean_samp <- X_mean_pop

# sample standard deviation 
X_sd_samp <- X_sd_pop / sqrt(n)

# P(A<x<B)=0.95, z=z, is (-zσ) - mean - (+zσ) e.g. z=1.96 -> (-1.96σ) - mean - (+1.96σ)
# z = ( x - µ ) / σ  -> x = ( z * σ) + µ
# lower value
A <- ( -z * X_sd_samp) + X_mean_samp
# upper values
B <- ( z * X_sd_samp) + X_mean_samp

cat(round(A, digits=2))
cat("\n")
cat(round(B, digits=2))

close(con)
