import pandas as pd

# name the header when import the data
Data_header = ['ID','Payment','Benefit_Amt']
NH_dat = pd.read_csv('Dataset_NoHead.csv', names=Data_header)
NH_dat.head()

# or 
NH_dat1 = pd.read_csv('Dataset_NoHead.csv', header = None)
NH_dat1.columns = Data_header

# Data with partial headers and renaming variables
PH_dat = pd.read_csv('Dataset_PartHead.csv')
PH_dat.head()
PH_dat = PH_dat.rename(columns={'Unnamed: 1':'Payment_Date'})