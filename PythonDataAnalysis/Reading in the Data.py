import pandas as pd
print "Pandas imported"

import os 
os.getcwd()  # current working directory
# os.chdir() to change current working directory

# Specify the path where the data is

# Reading the data
data = pd.read_csv("Dataset.csv",header=0)
data