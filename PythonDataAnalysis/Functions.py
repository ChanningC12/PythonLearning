def my_basic_function(a,b):
    print a**b
my_basic_function(3,4)

a = 10
def print_increment(a):
    a += 1
    print a
print_increment(a)
print a

def summed_squares(a,b,c):
    return a**2 + b**2 + c**2    
print summed_squares(1,2,3)
c = summed_squares(1,2,3)
print c    

def is_prime(numerator):
    denominator = 2
    isprime = "I do not know yet"
    while denominator <= numerator - 1:
        if numerator % denominator == 0:
            return False
        denominator += 1
        if denominator >= numerator: 
            return True
print 7, is_prime(7)
print 12131, is_prime(12131)

