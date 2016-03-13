# Sci-Kit-Learn is a central library for machine learning in python
# Contains most standard regression, clustering and modeling algorithms
# Features to modeling such as prepocessing, cross validation and data pipelines

import sklearn

# Load data because of great compatilibity with pandas
import pandas as pd
import numpy as np
# load csv
data = pd.read_csv("Dataset.csv",header=0).dropna()
data.head()

# transform data, scale data
numeric_data = data[['Benefit_Amt','Rent_Amount','Monthly_Benefit','Income']]
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler().fit(numeric_data)
scaler

# Obtain scaled data frame
scaled_numeric_matrix = scaler.transform(numeric_data)
scaled_numeric_matrix
# it produced a numpy array not pandas data frame
scaled_numeric_data = pd.DataFrame(scaled_numeric_matrix,columns = numeric_data.columns)
scaled_numeric_data

# can be done on one line
scaled_numeric_data = pd.DataFrame(MinMaxScaler().fit_transform(numeric_data),columns=numeric_data.columns)
scaled_numeric_data

# fit(dataset): build a model of the input dataset
# transform(dataset): using a model that has been produced apply it to the input dataset
# fit_transform: build a model and apply it to input dataset

from sklearn.cross_validation import KFold
n = 4
KFold(n,n_folds=3,shuffle=False,random_state=None)

scaled_numeric_matrix[0]
scaled_numeric_matrix[:,0]
scaled_numeric_matrix[:,1:3]
pd.DataFrame(scaled_numeric_matrix[3:6,1:3])
scaled_numeric_matrix[[1,3,5]]
scaled_numeric_matrix[scaled_numeric_matrix[:,1]>0.5]






