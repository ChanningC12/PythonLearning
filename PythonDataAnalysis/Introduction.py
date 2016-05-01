# CH2. Language Introduction
print 1+1

# print "1"+1 #TypeError: cannot concatenate 'str' and 'int' objects

a="1"
print type(a)
b=1
print type(b)

# User Defined Functions
def my_function(name):
    return "Have a nice day {}".format(name)

print my_function("CC")

# List 
things = ["Thing One","Thing Two"]
print type(things)
print len(things)
print things.pop()
print things
print things.append("Thing Two, welcome back!")
print things

# Diretionary
my_dictionary = {'something_unique':1, 'something_else_unique':2}
print type(my_dictionary)
print my_dictionary.keys()
print my_dictionary.values()

example = {1:1}
assign_me = example
assign_me[1]=2
print example

# Tuples
(1,2,3) != [1,2,3]
a = [1,2,3]
a[0]
b={1,2,3}
b[0]  # Tuple is immutable

set([1,2,3])==set([1,2,3,3,3])
set_1_to_3 = set([1,2,3])
set_2_to_4 = set([2,3,4])
print set_1_to_3 - set_2_to_4
print set_1_to_3 & set_2_to_4
print set_1_to_3 | set_2_to_4

# Import this (modules)
import this
my_dict={}
my_dict['a'] += 1 # a doesn't exist

from collections import defaultdict
my_default_dict = defaultdict(int)
my_default_dict['a'] += 1
print my_default_dict
print my_default_dict.items()

# anomymous functions
def f(x):
    return x**2
print f(4)

f2 = lambda x:x**2
f(100) == f2(100)

[x.upper() for x in things if x!='Thing One']

# Working directory
import os
os.getcwd()
os.chdir('/Users/chicheng/Desktop/Github/PythonLearning/PythonDataAnalysis')
# Open a file
fobj = open("Dataset.csv")
fobj.read(1024)
import csv
fobj.seek(0)
dialect = csv.Sniffer().sniff(fobj.read(1024))
print "dialect:",dialect.__dict__
fobj.seek(0)
reader = csv.DictReader(fobj,dialect=dialect)

list(reader)[:3]
fobj.seek(0)

# Enter Pandas
import pandas # like R dataframe
df = pandas.read_csv(open("Dataset.csv"))
print df

# plot it
df.plot(kind="scatter",x="Income",y="Rent_Amount")




















































