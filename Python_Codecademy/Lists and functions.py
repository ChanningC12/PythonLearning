n=[1,3,5]
print (n[1])

n[1]=n[1]*5
print(n)

n.append(4)
print (n)

n.pop(0)
print (n)

number=5
def my_function(x):
    return x*3

print (my_function(number))

m=5
n=13
def add_function(x,y):
    total=x+y
    return total
print (add_function(m,n))

q="hello "  
def string_function(s):
    return s+"world"
print (string_function(q))


def list_function(x):
    return x[1]
nn=[3,5,7]
print (list_function(nn))

def double_first(n):
    n[1]=n[1]+3
    return n
print (double_first(nn))

def list_extender(lst):
    lst.append(9)
    return lst
print (list_extender(nn))


def print_list(x):
    for i in range(0,len(x)):
        print (x[i])
print (print_list(nn))

nnn=[1,2,4,6,9]
def double_list(x):
    for i in range(0,len(x)):
        x[i]=x[i]*2
        return x
print (double_list(nnn))



    













