import panda as pd
import sklearn

# read in dataset
data = pd.read_csv('Dateset.csv')
data.head()
# create an indicator column for overpayment
data['Overpayment_ind'] = (data.Overpayment_Amount != ' ').astype(int)
data.columns

# construct and design matrix
from patsy import dmatrices
y, X = dmatrices('Overpayment_ind ~ Age_in_yrs + Income + \
                 Rent_Amount + Number_Children + C(Moved_from_out_of_state_12_mths) + \
                 C(Citizenship) + C(Previous_Felony)',
                 data, return_type='dataframe')

print X.columns

# rename indicator columns to a mroe readable form
X = X.rename(columns = {'C(Moved_from_out_of_state_12_mths)[T.Y]':'Moved_from_out_of_state_12_mths',
                         'C(Citizenship)[T.Verified]':'Citizenship_Verified',
                         'C(Previous_Felony)[T.Y]':'Previous_Felony'})
X.head()

import numpy as np
from sklearn.linear_model import LogisticRegression

ya = np.ravel(y)
model = LogisticRegression()
model = model.fit(X,ya)

model.score(X,ya)
1-ya.mean()

pd.DataFrame(zip(X.columns,np.transpose(model.coef_)))

# evaluate the model
from sklearn.cross_validation import train_test_split

# 30% test, 70% fit
X_train, X_test, y_train, y_test = train_test_split(X,ya,test_size=0.3,random_state=0)
model12 = LogisticRegression()
model12.fit(X_train,y_train)

predicted = model12.predict(X_test)
print predicted

probs = model12.predict_proba(X_test)
print probs

# ROC
from sklearn import metrics
# how many predicted labels match y_test labels?
print metrics.accuracy_score(y_test,predicted)
# what is the area under the curve statistic
print metrics.roc_auc_score(y_test,probs[:,1])

# ROC chart
from sklearn.metrics import roc_curve as sk_roc_curve
import matplotlib.pyplot as pl

def plot(y_test,predicted):
    fpr,tpr,thresholds = sk_roc_curve(y_test,predicted)
    
    # plot ROC curve
    pl.clf()
    pl.plot(fpr,tpr,"r")
    pl.plot([0,1],[0,1],'k--')
    pl.xlim([0.0,1.0])
    pl.ylim([0.0,1.0])
    pl.xlabel("False Positive Rate")
    pl.ylabel("True Positive Rate")
    pl.title('Receiver operating characteristics')
    pl.legend(loc="lower right")
    pl.show()

plot(y_test,probs[:, 1])    

print metrics.confusion_matrix(y_test,predicted)
print metrics.classification_report(y_test,predicted)

from sklearn.cross_validation import cross_val_score
scores = cross_val_score(LogisticRegression(),X,ya,scoring='accuracy',cv=10)
print scores
print scores.mean()

model.predict_proba(np.array([1,0,0,1,34,400,700,1]))






    
    
    
    
    






















