# challenge: https://www.hackerrank.com/challenges/s10-basic-statistics/problem

con <- file("stdin", open = "r")

dataset <- readLines(con)

v_values <- unlist(strsplit(dataset[2], split=" "))
v_values <- as.numeric(v_values)

mode <- function(v) {
    v_val_tab <- table(v_values)
    v_val_tab <- sort(v_val_tab, decreasing=TRUE)
    return(as.numeric(names(v_val_tab[1])))
}

cat(round(mean(v_values), digits=1))
cat("\n")
cat(round(median(v_values), digits=1))
cat("\n")
cat(mode(v_values))

close(con)
