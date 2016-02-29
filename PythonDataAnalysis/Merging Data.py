import pandas as pd
import os

# read in data
Part_dat = pd.read_csv('Dataset_Partial.csv',header=0)
Bamt_dat = pd.read_csv('Dataset_BenAmt.csv',header=0)
Nfam_dat = pd.read_csv('Dataset_NoFamily.csv',header=0)

# get dimensions
Part_dat.shape
Bamt_dat.shape
Nfam_dat.shape

# get column names
Part_dat.columns
Bamt_dat.shape
Nfam_dat.shape

# get first few observations
Part_dat.head(4)

# Database Style Merging
dat_temp = pd.merge(Part_dat,Bamt_dat,how='left', on = ['ID']) # Payment_Date didn't merge together
dat_temp.shape
# duplicates, to avoide, merge based on multiple columns
dat_temp1 = pd.merge(Part_dat, Bamt_dat, how='left', on=['ID','Payment_Date'])
dat_temp1.shape

# failed: data_temp3 = pd.merge(Part_dat, Nfam_dat, how= 'left', on=['ID'])
data_temp2 = pd.merge(Part_dat, Nfam_dat, how= 'left', left_on=['ID'], right_on=['KEY'])
dat_temp3 = pd.merge(dat_temp1, Nfam_dat, how='left', left_on=['ID'], right_on=['KEY'])
dat_temp3.head()

# export data
dat_temp3.to_csv("Merged_Data.csv",sep=",",header=True,index=False)