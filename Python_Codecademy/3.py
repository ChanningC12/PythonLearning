#3.1 strings
brian="Hello Life!"
print (brian)

#3.4 Access by Index
fifth_letter="Money"[4]
print (fifth_letter)

#3.5 strings method - length
parrot="Norwegian Blue"
print (len(parrot))

#3.6 lower upper
print (parrot.lower())
print (parrot.upper())

#3.8 turn into string
pi=3.14
print (str(pi))

#3.10 print strings
print ("Money Python")

#3.12 String Concatenation
print ("I "+"am "+"CC!")

#3.13 Explicit String Conversion
print ("The value of pi is around "+str(3.14))

#3.14 String Formatting with %, Part1
string_1="Qifeng"
string_2="CC"

print("%s is zhuangbi, %s is niubi." % (string_1,string_2))

#3.15 String formatting part2
name = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")

print ("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))

