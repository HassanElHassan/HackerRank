# challenge: https://www.hackerrank.com/challenges/s10-weighted-mean/problem

con <- file("stdin", open = "r")
dataset <- readLines(con)
ls_grade <- unlist(strsplit(dataset[2], split=" "))
ls_grade <- as.numeric(ls_grade)
ls_weight <- unlist(strsplit(dataset[3], split=" "))
ls_weight <- as.numeric(ls_weight)

mult = ls_grade*ls_weight
mult_sum = sum(mult)
weight_sum = sum(ls_weight)

cat(format(round(mult_sum/weight_sum, digits=1), nsmall=1))

close(con)
