import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import locale

# A hello world matplotlib plot
plt.plot(range(20))
plt.show()

fig = plt.figure(figsize=[4,4])
ax1 = fig.add_axes([0,0,1,1])
ax1.plot(range(20))
fig.show()

# another example
import numpy as np
fig = plt.figure(figsize=[12,12])
ax1=fig.add_axes([0,0,1,1])
# set the number of points to be displayed
numpoints=100
# we want to color the points randomly
rgba_colors = np.zeros((numpoints,4))
# fill in first 3 columns with random percentage for red, green, blue
for ii in range(0,3):
    rgba_colors[:,ii] = np.random.uniform(low=0.1,high=0.9,size=numpoints)
# the fourth column sets the transparency
rgba_colors[:,3] = np.random.uniform(low=0.1,high=0.9,size=numpoints)

ax1.scatter(np.random.random_integers(low=0,high=100,size=numpoints),
            np.random.random_integers(low=0,high=100,size=numpoints),
            s=np.random.random_integers(low=100,high=500,size=numpoints),
            color=rgba_colors)
fig.show()


# plot with pandas
Data = pd.read_csv("Dataset.csv")
Data['ID'].head()

Data.Benefit_Amt.hist(figsize=[8,6])
Data[['Benefit_Amt','Citizenship']].hist(by='Citizenship',figsize=[8,6])

mark = Data['Overpayment_Amount']==' '
Data['Overpayment_amt']=Data['Overpayment_Amount']
Data.ix[mark,'Overpayment_amt']=0
Data['Overpayment_amt']=Data['Overpayment_amt'].apply(lambda x:float(x))

Data.ix[Data['Overpayment_amt']>0,['Overpayment_amt','Citizenship']].hist(by='Citizenship',figsize=[16,6])
# scatter plot
Data.plot(kind='scatter',x='Rent_Amount',y='Monthly_Benefit',figsize=[10,8],s=100)
Data[Data['Overpayment_amt']>0].plot(kind='scatter',x='Rent_Amount',y='Monthly_Benefit',figsize=[10,8],s=100)
















