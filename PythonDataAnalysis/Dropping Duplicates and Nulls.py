import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

Data = pd.read_csv("Dataset.csv")

# dropping duplicates
len(Data['ID'])
Data['ID'].duplicated().head(10)

Data_dd = Data.drop_duplicates(['ID'])
Data_dd['ID'].duplicated().head()
# by default, drop_duplicated will keep the first duplicated observation
# use take_last = True keep the last observation
Data_dd2 = Data.drop_duplicates(['ID'],take_last=True)
Data_dd2.head()

# dropping NAs
Data['Overpayment_Amount'] = Data['Overpayment_Amount'].convert_objects(convert_numeric=True)
NONA1 = Data[np.isfinite(Data['Overpayment_Amount'])]
# isfinite works but is a confusing usage because NaN is technically neither finite or infinite
NONA1.shape
NONA1[['ID','Overpayment_Amount','Benefit_Amt']].head()

NONA2 = Data[np.isnan(Data['Overpayment_Amount'])==False]
NONA2.head()
NONA2.shape

# An easier way, and more straightforward way to drop NAs is:
NONA3 = Data.dropna(subset=['Overpayment_Amount'])
NONA3.shape

# using both drops at once
DDN = Data.dropna(subset=['Overpayment_Amount']).drop_duplicates(['ID'],take_last=True)
DDN.shape