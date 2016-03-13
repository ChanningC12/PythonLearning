# load in standard data libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
data = pd.read_csv('Dataset.csv',header=0).dropna()
data.head()

# create feature sets
# use benefit amount as pricipal output
benefit_amt = data['Monthly_Benefit']

# start with simple univariate selecting Income as the sole
# indepedent variable
features = data['Income']
features = np.array(features).reshape(features.shape[0],1)

# LS regression
from sklearn.linear_model import LinearRegression
linear_modeler = LinearRegression()

linear_model = linear_modeler.fit(features,benefit_amt)
print "Our coefficient value for Income", linear_model.coef_
print "Our intercept value", linear_model.intercept_

# R-square
import sklearn.metrics
print sklearn.metrics.r2_score(benefit_amt,linear_model.predict(features))

# rebuild model
features = data[['Age_in_yrs','Income','Rent_Amount','Number_Adults','Number_Children']]
linear_model = linear_model.fit(features,benefit_amt)
print "Our coefficient value:"
print np.array([['Age_in_yrs','Income',"Rent_Amount","Number_Adults","Number_Children"],list(linear_model.coef_)])
print "Our intercept value", linear_model.intercept_
print sklearn.metrics.r2_score(benefit_amt,linear_model.predict(features))

# Visualize the model
residual = linear_model.predict(features)-benefit_amt
# a good residual plot should have balanced distribution around the regression line
nozeros = data['Income']>0
plt.scatter(data['Income'][nozeros],residual[nozeros])
plt.axhline(y=0,color='red')
plt.show()

# another way to view distribution of model residual around the regression line is to a histogram of the residual
plt.hist(residual,50)
plt.axvline(x=0,color='red')
plt.show()

# Pandas has a bulit-in OLS function
pd.ols(y=benefit_amt,x=features)

# Learning curves show how much additional data improves the performance of our linear regression model
# Learning curves can be used to evaluate performance of many different types of supervised models
from sklearn.learning_curve import learning_curve
bins, train_scores, test_scores=learning_curve(
    linear_model,
    features,
    benefit_amt,
    train_sizes=np.arange(.1,1,.01))
    
# plot performance of test data versus training data
plt.plot(bins,np.mean(train_scores,axis=1),color='blue',label='training')
plt.plot(bins,np.mean(test_scores,axis=1,color='red',label='scoring')
plt.xlabel("Trianing examples")
plt.ylabel("Score")
plt.legend()
plt.show()


















