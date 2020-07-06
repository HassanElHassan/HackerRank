# https://www.hackerrank.com/challenges/s10-standard-deviation/problem

# the build in sd() function is for sample not population
# an option -> sqrt((n-1)/n) * sd(x)

# function to calculate the population sd
popsd <- function(v_val){
    # average the elements in the vector
    v_val_avg <- mean(v_val)
    # squared distance from the mean
    v_val_dist <- (v_val-v_val_avg)^2
    # average squared distance from the mean
    v_val_dist_avg <- sum(v_val_dist) / length(v_val)
    # SD by square root of average squared distance from the mean
    sqrt(v_val_dist_avg)
}   

con <- file("stdin", open = "r")

dataset <- readLines(con)

v_val <- unlist(strsplit(dataset[2], split=" "))
v_val <- as.numeric(v_val)

cat(round(popsd(v_val),digits=1))

close(con)
