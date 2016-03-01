# sort using data.table
library(data.table)
dataframe = as.data.table(df)
dataframe[order(c3)]
dataframe[order(c1,-c2)]

# By default, ascending

