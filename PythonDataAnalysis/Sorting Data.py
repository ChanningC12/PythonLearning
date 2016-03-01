import pandas as pd
Data = pd.read_csv('Dataset.csv',header=0)

# basic sorting
a = [3, 5, 4, 1, 2]
sorted(a) # Ascending by dafault
sorted(a, reverse = True) # Descending

Data.columns.tolist()
Data2 = Data
sorted(Data2['ZipCodes'])
sorted(Data2['ZipCodes'], reverse=True)

# sort more complex data, like a list of dictionaries
list_to_be_sorted = [{'name':'bob','score':90},
                     {'name':'sue','score':76},
                     {'name':'ted','score':65},
                     {'name':'mary','score':100}]
                     
def sorter(row):
    return row['name']

sorted(list_to_be_sorted, key = lambda k: k['score'],reverse=True)
sorted(list_to_be_sorted, key = lambda k: k['name'], reverse=True)