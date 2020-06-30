# challenge: https://www.hackerrank.com/challenges/s10-weighted-mean/problem

con <- file("stdin", open = "r")

dataset <- readLines(con)

v_grade <- unlist(strsplit(dataset[2], split=" "))
v_grade <- as.numeric(v_grade)

v_weight <- unlist(strsplit(dataset[3], split=" "))
v_weight <- as.numeric(v_weight)

mult = v_grade*v_weight
mult_sum = sum(mult)
weight_sum = sum(v_weight)

cat(format(round(mult_sum/weight_sum, digits=1), nsmall=1))

close(con)
