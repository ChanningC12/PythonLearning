# Summary and Descriptive
# Basic sums and means

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

import os
os.getcwd()
os.chdir("/Users/chicheng/Desktop/Github/PythonLearning/PythonDataAnalysis")

Data = pd.read_csv('Dataset.csv')
Data['Overpayment_Amount']=Data['Overpayment_Amount'].convert_objects(convert_numeric=True)
Data['Dollar_Error1']=Data['Dollar_Error1'].convert_objects(convert_numeric=True)
Data['Dollar_Error2']=Data['Dollar_Error2'].convert_objects(convert_numeric=True)
Data['Dollar_Error3']=Data['Dollar_Error3'].convert_objects(convert_numeric=True)
Data.head()

# sum, mean
Data['Benefit_Amt'].sum()
Data['Benefit_Amt'].mean()

# describe
Data['Benefit_Amt'].describe()

# Group by
Data.groupby(['ZipCodes'])['Benefit_Amt'].sum()
Data.groupby(['ZipCodes'])['Benefit_Amt'].mean()
Data.groupby(['ZipCodes'])['Benefit_Amt'].count()
Data.groupby(['Citizenship'])['ID'].nunique() # number of unique

Data.groupby(['ZipCodes','Previous_Felony'])['Benefit_Amt','Income'].sum()

Data.groupby(['ZipCodes'])['Benefit_Amt'].agg([np.sum,np.mean,np.size])

Data.groupby(['ZipCodes'])['Benefit_Amt'].agg({'QF':np.sum,'QQQF':np.mean,'QQF':np.size})

# What is the average income by marries and citizenship status
Data.groupby(['Marital_Status','Citizenship'])['Income'].mean()
# What is the total Benefit and Overpayment amount by Date
Data.groupby(['Payment_Date'])['Benefit_Amt','Overpayment_Amount'].sum()
# What is the sum, mean, and standard deviation of Overpayment amount by zip code
Data.groupby(['ZipCodes'])['Overpayment_Amount'].agg([np.sum,np.mean,np.std])
# How many unique IDs by previous felony
Data.groupby(['Previous_Felony'])['ID'].nunique()

# Value_counts
Data['ZipCodes'].value_counts()
Data.groupby(['ZipCodes'])['ZipCodes'].count()
pd.value_counts(Data['ZipCodes'])

# corr() and cov()
Data[['Medical_Expense_Amount','Dependent_Care_Amount']].corr(method='pearson',min_periods=1)
Data[['Number_Children','Benefit_Amt']].corr(method='pearson',min_periods=1)

cor = Data.corr(method='pearson',min_periods=1)
cor



































