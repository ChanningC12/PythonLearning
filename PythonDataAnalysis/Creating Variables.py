import pandas as pd
import numpy as np

Data = pd.read_csv('Dataset.csv',header=0)
Data.head()

# make a copy of another variable
a = [5,3,4,2,11,13,38]
b = a
b

Data['Copy_of_Benefit'] = Data['Benefit_Amt']
Data.head()

# binning a variable
Data['Benefit_Amt_gt_200'] = np.where(Data['Benefit_Amt']>=200,1,0)
Data['Benefit_Amt_lt_200'] = np.where(Data['Benefit_Amt']<200,2,0)
Data[['ID','Benefit_Amt','Benefit_Amt_gt_200','Benefit_Amt_lt_200']].head(10)


