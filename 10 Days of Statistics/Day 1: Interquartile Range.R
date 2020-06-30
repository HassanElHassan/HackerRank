# https://www.hackerrank.com/challenges/s10-quartiles/problem

# quartiles calculated based on the first method described in the Wikipedia:
# https://en.wikipedia.org/wiki/Quartile#Method_1
# none of the 9 types available in the R function quantile are according to this methode

Q1_Q3 <- function(v_values){
    # sort vector
    v_values <- sort(v_values)
    # number of elements in vector
    len_v <- length(v_values)
    # if number of elements is even e.g. 1,2,3,4,5,6,7,8,9,10
    if(len_v%%2==0) {
        # end of lower half will be len/2 e.g. 10/2 = 5
        end_lower <- len_v/2
        # start of upper half will be end of lower half plus 1 e.g. 5+1=6
        start_upper <- end_lower + 1
    }
    # if number is uneven e.g. 1,2,3,4,5,6,7,8,9,10,11
    else {
        # middle number e.g. (11+1)/2=6
        mid <- (len_v+1)/2
        # end of lower half will be mid minus 1 e.g. 6-1=5
        end_lower = mid - 1
        # start of upper half will be mid plus 1 e.g. 6+1=7
        start_upper = mid + 1
    }
    c(
        Q1=median(v_values[1:end_lower]),
        Q3=median(v_values[start_upper:len_v])
        )  
}

con <- file("stdin", open = "r")

dataset <- readLines(con)

v_elem <- unlist(strsplit(dataset[2], split=" "))
v_elem <- as.numeric(v_elem)

v_freq <- unlist(strsplit(dataset[3], split=" "))
v_freq <- as.numeric(v_freq)

v_values <- rep(v_elem, v_freq)

Q1_Q3_values <- Q1_Q3(v_values)
Q1 <- Q1_Q3_values[1]
Q3 <- Q1_Q3_values[2]

# format to keep the zero after the decimal point
cat(format(round(Q3-Q1, digits=1), nsmall = 1))

close(con)
