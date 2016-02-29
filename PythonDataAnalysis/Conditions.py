x = 2
print "Does x=3? And the Answer is" 
print x==3

x=2
y=4
if x==2 and y==x*x:
    print "y equals x*x"
    print "{} equals {}*{}".format(y,x,x)
    print "%s equals %s*%s" % (y,x,x)
    print "{y} equals {x}*{x}".format(y=y,x=x)
    print "{y} equals {x}*{x}".format(**locals())
    print "{y} equals {x}*{x}".format(**dict(y=y,x=x))
    
if x==2:
    print "x equals two"
else:
    print "x equals: ",x
    
choice = raw_input("Enter a letter: ")
if choice == "a":
    print "You chose 'a'."
elif choice == "b":
    print "You chose 'b'."
else:
    print "I do not understand!"

