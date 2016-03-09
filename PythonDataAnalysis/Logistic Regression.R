# read the dataset
dta = read.csv("Desktop/Github/PythonLearning/PythonDataAnalysis/dta.csv")
# Description of Variables
# rate_marriage: woman's rating of her marriage (1 = very poor, 5 = very good)
# age: woman's age
# yrs_married: number of years married
# children: number of children
# religious: woman's rating of how religious she is (1 = not religious, 4 = strongly religious)
# educ: level of education (9 = grade school, 12 = high school, 14 = some college, 16 = college graduate, 17 = some graduate school, 20 = advanced degree)
# occupation: woman's occupation (1 = student, 2 = farming/semi-skilled/unskilled, 3 = "white collar", 4 = teacher/nurse/writer/technician/skilled, 5 = managerial/business, 6 = professional with advanced degree)
# occupation_husb: husband's occupation (same coding as above)
# affairs: time spent in extra-marital affairs

library(data.table)
dta=as.data.table(dta)
summary(dta$affairs)
dta$affair = ifelse(dta$affairs>0,1,0)
table(dta$affair)