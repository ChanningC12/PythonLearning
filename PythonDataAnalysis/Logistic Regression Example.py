# Data School: http://www.dataschool.io/logistic-regression-in-python-using-scikit-learn/
# https://github.com/justmarkham/gadsdc1/blob/master/logistic_assignment/kevin_logistic_sklearn.ipynb
# The dataset I chose is the affairs dataset that comes with Statsmodels. 
# It was derived from a survey of women in 1974 by Redbook magazine, 
# in which married women were asked about their participation in extramarital affairs. 
# More information about the study is available in a 1978 paper from the Journal of Political Economy.

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

# import module
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

from patsy import dmatrices
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score

# data pre-processing
# load dataset
dta = sm.datasets.fair.load_pandas().data
dta.head()

# export data
dta.to_csv('dta.csv',index=False)

# add "affair" column: 1 represents having affairs, 0 not
dta['affair'] = (dta.affairs>0).astype(int)
dta.head()
dta.groupby('affair').mean()
dta.groupby('rate_marriage').mean()

# data visualization
# histogram of education
dta.educ.hist()
plt.title("Histogram of Education")
plt.xlabel("Education Level")
plt.ylabel("Frequency")
# equals
dta.groupby('educ').count()

# histogram of marriage rating
dta.rate_marriage.hist()
plt.title('Histogram of Marriage Rating')
plt.xlabel('Marriage Rating')
plt.ylabel('Frequency')

# barplot of marriage rating grouped by affair (T or F)
pd.crosstab(dta.rate_marriage,dta.affair.astype(bool)).plot(kind='bar')
plt.title('Marriage Rating Distribution by Affair Status')
plt.xlabel('Marriage Rating')
plt.ylabel('Frequency')

# stacked barplot 
affair_yrs_married = pd.crosstab(dta.yrs_married,dta.affair.astype(bool))
affair_yrs_married.div(affair_yrs_married.sum(1).astype(float),axis=0).plot(kind='bar',stacked=True)
plt.title('Affair Percentage by Years Married')
plt.xlabel('Years Married')
plt.ylabel('Percentage')


# Prepare Data for Logistic Regression
y, X = dmatrices('affair ~ rate_marriage + age + yrs_married + children + \
                  religious + educ + C(occupation) + C(occupation_husb)',
                  dta, return_type = "dataframe")
print X.columns

X = X.rename(columns = {'C(occupation)[T.2.0]':'occ_2',
                        'C(occupation)[T.3.0]':'occ_3',
                        'C(occupation)[T.4.0]':'occ_4',
                        'C(occupation)[T.5.0]':'occ_5',
                        'C(occupation)[T.6.0]':'occ_6',
                        'C(occupation_husb)[T.2.0]':'occ_husb_2',
                        'C(occupation_husb)[T.3.0]':'occ_husb_3',
                        'C(occupation_husb)[T.4.0]':'occ_husb_4',
                        'C(occupation_husb)[T.5.0]':'occ_husb_5',
                        'C(occupation_husb)[T.6.0]':'occ_husb_6'})
print X.columns
print y
print X

# flatten y into 1-D array
y = np.ravel(y)

# Logistic Regression
## instantiate a logistic regression model and fit with X and y
model = LogisticRegression()
model = model.fit(X,y)

# check the accuracy on the training set
model.score(X, y)

# what percentage had affairs
y.mean()

# examine the coefficients
pd.DataFrame(zip(X.columns,np.transpose(model.coef_)))

# model evaluation using a validation set
# evaluate the model by splitting into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=0)
model2 = LogisticRegression()
model2.fit(X_train, y_train)

# predict class labels for the test set
predicted = model2.predict(X_test)
print predicted

# generate class probabiliies
probs = model2.predict_proba(X_test)
print probs

# generate evaluation metrics
print metrics.accuracy_score(y_test,predicted)
print metrics.roc_auc_score(y_test,probs[:,1])

# model evaluation using cross-validation
# evaluate the model using 10-fold cross-validation
scores = cross_val_score(LogisticRegression(),X,y,scoring='accuracy',cv=10)
print scores
print scores.mean()

# predicting the probability of an Affair
model.predict_proba(np.array([1,0,0,1,0,0,1,0,0,0,0,3,25,3,1,4,16]))








































