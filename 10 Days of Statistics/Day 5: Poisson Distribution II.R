# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

con <- file("stdin", open = "r")

dataset <- unlist(strsplit(readLines(con), split="\\s"))

# mean of A
A <- as.numeric(dataset[1])
# mean of B
B <- as.numeric(dataset[2])

# expected daily cost of machine A using E[X**2] = lambda + lambda**2
A_cost <- 160 + 40 * (A + A**2)
# expected daily cost of machine B using E[X**2] = lambda + lambda**2
B_cost <- 128 + 40 * (B + B**2)

cat(round(A_cost, digits=3))
cat("\n")
cat(round(B_cost, digits=3))

close(con)
