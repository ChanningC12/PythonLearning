import pandas as pd
Data = pd.read_csv("Dataset.csv")

List_nulls = pd.DataFrame({'one':(1,3,8,6,9),
                           'two':(8,0,1,2,6)},
                            index = ['a','c','e','f','g'])
List_nulls

List_nulls2 = List_nulls.reindex(['a','b','c','d','e','f','g','h'])
List_nulls2

# pandas has a fillna function to "fill in" NA values with non-null data in a couple of ways
# 1. fill with zero
List_nulls2.fillna(0)
List_nulls2.fillna(999)

# 2. fill with the mean, column mean
List_nulls2.fillna(List_nulls2.mean())
List_nulls2.mean()

# 3. fill with the maximum number
List_nulls2.fillna(List_nulls2.max())

# 4. fill with the minimum number
List_nulls2.fillna(List_nulls2.min())


