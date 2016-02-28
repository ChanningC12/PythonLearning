#looping over a dictionary
d={'a':'apple','b':'berry','c':'cherry'}
for key in d:
    print (key,d[key])

#counting as you go
choices = ['pizza', 'pasta', 'salad', 'nachos']

print ('Your choices are:')
for index, item in enumerate(choices):
    print (index+1, item)

#multiple list
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a,b in zip(list_a,list_b):
    if a<b:
        print (a)
    if a>b:
        print (b)

#for / else
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ('You have...')
for f in fruits:
    if f == 'tomato':
        print ('A tomato is not a fruit!') # (It actually is.)
        break
    print ('A', f)
else:
    print ('A fine selection of fruits!')

#Change it up
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ('You have...')
for f in fruits:
    if f == 'tomato':
        print ('A tomato is not a fruit!') # (It actually is.)
    print ('A', f)
else:
    print ('A fine selection of fruits!')
