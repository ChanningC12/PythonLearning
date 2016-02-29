my_list=[]
my_dict={}
my_tuples = ()

print type(my_list)
print type(my_dict)
print type(my_tuples)

my_list.append(1)
print my_list

my_set = set(my_list)
type(my_set)
my_set == my_list

import time
a_long_list = list(range(100000))
a_long_set = set(a_long_list)

def we_time_it(f):
    time1 = time.time()
    f()
    time2 = time.time()
    print 'took %0.3f ms' % ((time2-time1)*1000.0)
    
# More on Dictionaries
my_dict = {'a':1,'b':2,'c':3,5:'d'}
my_dict.keys()
my_dict.values()
print "\n".join(["key: '{}' value: '{}'".format(k,v) for k,v in my_dict.items()])



import pandas as pd
df = pd.DataFrame.from_csv("Dataset.csv")
df.to_dict()

# Special Ordered Dict
from collections import OrderedDict
ordered_dict = OrderedDict(a=1,b=2,c=3)
regular_dict = dict(a=1,b=2,c=3)
ordered_dict[1] = 4
regular_dict[1] = 4
ordered_dict
regular_dict













