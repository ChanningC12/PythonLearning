# load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import warnings
warnings.filterwarnings('ignore')
import IPython
data = pd.read_csv("Dataset.csv",header=0).dropna()

hd_data = pd.DataFrame()
hd_data['Benefit_Amt']=data['Benefit_Amt']
hd_data['Income']=data['Income']
hd_data['Rent_Amount']=data['Rent_Amount']
hd_data['Monthly_Benefit']=data['Monthly_Benefit']
# some numeric data we will convert to binary or bin
hd_data['has_overpayment_amount']=(data['Overpayment_Amount'].convert_objects(convert_numeric=True)>0).astype(int)
hd_data['has_dollar_error']=((data['Dollar_Error1']+data['Dollar_Error2']+data['Dollar_Error3']).convert_objects(convert_numeric=True)>0).astype(int)
hd_data['has_dependent_care_amt']=(data['Dependent_Care_Amount']>0).astype(int)
hd_data['has_med_exp_amt']=(data['Medical_Expense_Amount']>0).astype(int)
hd_data['has_child_support_amt']=(data['Child_Support_Amount']>0).astype(int)

# some numeric data we will bin using a combination of the cut command and a loop
age_groups = pd.qcut(data['Age_in_yrs'],5)
for age_group in age_groups.unique():
    hd_data['age_group_%s' % age_group]=(age_groups==age_group).astype(int)
# other numerics we will use the get_dummies function
hd_data = pd.concat([hd_data,pd.get_dummies(data['Number_Adults'],prefix='adults')],axis=1)
hd_data = pd.concat([hd_data,pd.get_dummies(data['Number_Children'],prefix='children')],axis=1)

# convert all categoricals
hd_data = pd.concat([hd_data,pd.get_dummies(data['Citizenship'],prefix='citizen')],axis=1)
hd_data = pd.concat([hd_data,pd.get_dummies(data['ZipCodes'],prefix='zip')],axis=1)
hd_data = pd.concat([hd_data,pd.get_dummies(data['Marital_Status'],prefix='marital')],axis=1)
hd_data = pd.concat([hd_data,pd.get_dummies(data['Previous_Felony'],prefix='felony')],axis=1)
hd_data = pd.concat([hd_data,pd.get_dummies(data['Moved_from_out_of_state_12_mths'],prefix='moved')],axis=1)

hd_data.head()

# compare the original with the new dataset
IPython.display.display("Total number of variables in the original: %s" % len(data.columns),
                        data.describe())
IPython.display.display("Total number of variables in the new: %s" % len(hd_data.columns),
                        hd_data.describe())
                        
# data normalization before running PCA, mean(zero),sd(one) for all features
from sklearn.preprocessing import StandardScaler
hd_data_sd = StandardScaler().fit_transform(hd_data)
pd.DataFrame(hd_data_sd,columns=hd_data.columns).describe()

# run PCA on new dataset
from sklearn.decomposition import PCA
pca=PCA(copy=True,n_components=None)
pca_results=pca.fit(hd_data_sd)
print pca_results

n_components=len(pca_results.explained_variance_ratio_)
plt.figure(figsize=(15,5))
plt.bar(left=np.arange(n_components)+.5,height=pca_results.explained_variance_ratio_)
plt.xticks(np.arange(n_components)+1)
plt.xlabel("Principal Components")
plt.ylabel("Proportion of Total Variation")
plt.title("Proportion of Total variation carried per principal compenent")
plt.show()
IPython.display.display("Total variation in top 2 companies: %%%s" % np.round(100*np.sum(pca_results.explained_variance_ratio_[0:2]),2))
IPython.display.display("Total variation in top 27 companies: %%%s" % np.round(100*np.sum(pca_results.explained_variance_ratio_[0:27]),2))

# how do we obtain these components
X = pca_results.components_[0:2, :].dot(hd_data_sd.T).T
plt.scatter(X[:,0],X[:,1])
plt.show()

X = PCA(copy=True,n_components=2).fit_transform(hd_data_sd)
plt.scatter(X[:,0],X[:,1])
plt.show()







