names=["Adam","Alex","Mariah","Martine","Columbus"]

for i in names:
    print (i)

#Key
webster={"Aardvark":"A star of a popular children's cartoon show.","Baa":"The sound a goat makes."}
for key in webster:
    print (webster[key])

#Condition
a=[0,1,2,3,4,5,6,7,8]

for i in a:
    if i>7:
        print (i)

#list + function
def fizz_count(x):
    count=0
    for it in x:
        if it=="fizz":
            count=count+1
        return count

fizz_flam=["fizz","foz","foik","fizz","fizz"]
fozzy=fizz_count(fizz_flam)
print (fozzy)

#supermarket
price={"banana":4,"apple":2,"orange":1.5,"pear":3}
stock={"banana":6,"apple":0,"orange":32,"pear":15}
total=0
for key in price:
    print (key)
    print ("price: %s" %price[key])
    print ("stock: %s" %stock[key])
    total=total+price[key]*stock[key]
    print (total)


groceries=["banana","orange","apple"]
shopping_list=["banana","orange","apple"]

def compute_all(food):
    total=0
    for n in food:
        if stock[n]>0:
            total += price[n]
        stock[n]-=1
        return total

print (compute_all(shopping_list))










