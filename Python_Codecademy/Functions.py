def tax(bill):
    """Adds 8% tax to a restaurant bill"""
    bill *= 1.08
    print ("With tax: %f" % bill)
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill"""
    bill *= 1.15
    print ("With tip: %f" % bill)
    return bill

meal_cost=100
meal_with_tax=tax(meal_cost)
meal_with_tip=tip(meal_with_tax)

def square(n):
    """Returns the square of a number."""
    squared = n**2
    print ("%d squared is %d." % (n, squared))
    return squared
    
# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square(10)

def power(base,exponent):
    result=base**exponent
    print ("%d to the power of %d is %d" % (base,exponent,result))
    return result
power(5,4)


import math
print (math.sqrt(25))

from math import sqrt
print (sqrt(36))

#universal import
from math import *

#shows functions that are included in math
everything=dir(math)
print (everything)


#Putting *args and/or **kwargs as the last items in your function definition’s argument list allows that function to accept an arbitrary number of arguments and/or keyword arguments.
def biggest(*args):
    print (max(args))
    return (max(args))

def smallest(*args):
    print (min(args))
    return (min(args))

def distance(arg):
    print (abs(arg))
    return (abs(arg))

biggest(-10,5,3,2)
smallest(-34,21,-45,43)
distance(-42)










