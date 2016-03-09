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
mean(dta$affair)

# initial logistic model
dtalogit = glm(affair~rate_marriage + age + yrs_married + children
               + religious + educ + as.factor(occupation) + as.factor(occupation_husb),
                data = dta, family=binomial)
summary(dtalogit)
plot(dtalogit)

# stepwise regression to auto select variables
dtalogit2 = step(dtalogit,scope~rate_marriage + age + yrs_married + children
                 + religious + educ + as.factor(occupation) + as.factor(occupation_husb),test='F')

# simplified stepwise regression
dtalogit3 = glm(affair ~ rate_marriage + age + yrs_married + religious + as.factor(occupation),
                data=dta,family=binomial)
summary(dtalogit3)

# train, test, validation
# use the remaining data, colled the estimation or training sample, to build your model.
# The training set should be large enough to make reliable estimates
set.seed(12345)
dta$train = runif(nrow(dta))>0.5 # assign to test / train set 
table(dta$train)
dtalogit4 = glm(affair ~ rate_marriage + age + yrs_married + religious + as.factor(occupation),
                data=dta,subset=train,family=binomial)
summary(dtalogit4)
deviance(dtalogit4)
mean(dtalogit4$residuals^2)
yhat = predict(dtalogit4,dta[!dta$train,])
length(yhat)
mean((dta))









