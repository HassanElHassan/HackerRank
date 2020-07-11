# https://www.hackerrank.com/challenges/s10-multiple-linear-regression/problem

con <- file("stdin", open = "r")

dataset <- readLines(con)

# number of observed features (m) and  number of feature sets studied (n), str to int
m_n <- unlist(strsplit(dataset[1], split=" "))
m_n <- as.numeric(m_n)
m <- m_n[1]
n <- m_n[2]

# Each of the n subsequent input lines contain m+1 space-separated decimals
n_lines <- as.numeric(unlist(strsplit(dataset[2:(n+1)], split=" ")))
n_lines <- matrix(n_lines,ncol=m+1 ,nrow=n, byrow = TRUE)
# the first m elements are features (f1,f2,..)
X <- n_lines[,1:m]
# create matrix of shape 1 column and n rows to be used for calculating a  
X_a <- matrix(1,ncol=1,nrow=n)
# add the value 1 matrix to the X matrix that contains the features
X <- cbind(X_a,X)
# and the last element, m+1, is the value of Y for the line's feature set, drop=FALSE to keep Matrix data type
Y <- n_lines[,m+1, drop=FALSE]

# number of feature sets Andrea wants to query for
q <- dataset[n+2]
q <- as.numeric(q)

# Each of q contains m space-separated decimals describing the feature sets
X_query <- as.numeric(unlist(strsplit(dataset[(n+3):(n+3+q-1)], split=" ")))
X_query <- matrix(X_query,ncol=m ,nrow=q, byrow = TRUE)
# create matrix of shape 1 column and n rows to be used to multiply with a  
X_query_a <- matrix(1,ncol=1,nrow=q)
# add the value 1 matrix to the X matrix that contains the features
X_query <- cbind(X_query_a,X_query)

# find the Matrix B, .T to transpose and @ for matrix multiplication
# Y = X*B  ->  X.T*Y = X.T*X*B  ->  B = inv(X.T*X)*X.T*Y
B <- solve(t(X)%*%X)%*%t(X)%*%Y

# find the value of Y for each of the q feature sets
Y_query <- X_query%*%B

cat(round(Y_query,digits=2), sep="\n")
