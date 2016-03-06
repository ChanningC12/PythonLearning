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

















