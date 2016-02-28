zoo_animals=["pangolin","cassowary","sloth","lion"];

if len(zoo_animals)>3:
    print ("The first animal at the zoo is the "+ zoo_animals[0])
    print ("The second animal at the zoo is the "+ zoo_animals[1])
    print ("The third animal at the zoo is the "+ zoo_animals[2])


number=[5,6,7,8]

print ("Adding the numbers at indices 0 and 2...")
print (number[0]+number[2])
print ("Adding the numbers at indices 1 and 3...")
print (number[1]+number[3])

#Change the content
zoo_animals[2]="hyena"
print (zoo_animals)

suitcase=[]
suitcase.append("sunglasses")
suitcase.append("houses")
suitcase.append("phones")
suitcase.append("cars")

list_length=len(suitcase)

print ("There are %d items in the suitcase" %(list_length))

#List Slicing
suitcase=["sunglasses","hat","passport","laptop","suit","shoes"]
first=suitcase[0:2]
print (first)

name="catdogfrog"
cat=name[:3]
print (cat)

#Maintaining order
suitcase.insert(1,"phone")
print (suitcase.index("hat"))

#For one and all
my_list=[1,3,4,5,6,7]
for i in my_list:
    print (2*i)

#More with "for"
start_list=[5,3,1,2,4]
square_list=[]
for x in start_list:
    square_list.append(x**2)
    square_list.sort()
    print (square_list)

residents={"Puffin":104,"Sloth":105,"Burmese Python":106}
print (residents["Puffin"])

#New Entries
menu={}
menu["Chicken Alfredo"]=14.50
print (menu["Chicken Alfredo"])

menu["Bacon"]=3
menu["Burger"]=4

print ("There are " + str(len(menu)) + " items on the menu")
print (menu)

del menu["Bacon"]
menu["Burger"]=5

print (menu)


#Final Review
inventory={
    "gold":500,
    "pouch":["flint","twine","gemstone"],
    "backpack":["xylophone","dagger","bedroll","bread loaf"]
    }

inventory["burlap bag"]=["apple","small ruby","three-toed sloth"]

inventory["pouch"].sort()

inventory["backpack"].remove("dagger")
inventory["gold"]+=50
print (inventory)





















