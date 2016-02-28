count=0
#Difference between if and while
if count<5:
    print ("Hello! I am an if statement and count is ", count)

while count<=5:
    print ("Hello! I am a while and count is ", count)
    count += 1

#Condition
loop_condition=True
while loop_condition:
    print ("I am a loop")
    loop_condition=False

#While you are at it
num=1
while num<=10:
    print (num**2)
    num+=1

#Simple error
choice=input("Enjoying the course?(y/n)")
while choice != 'y' and choice != 'n':
    choice=input("Sorry, I didn't catch that. Enter again: ")


#Infinite loops
channing=0
while channing<10:
    print (channing)
    channing += 1

#Break
cheng=0
while True:
    print (cheng)
    cheng += 1
    if cheng >=10:
        break

#While/else
import random
print ("Lucky Numbers! 3 numbers will be generated!")
print ("If one of them is a '5', you lose!")

cc=0
while cc<3:
    num=random.randint(1,6)
    print (num)
    if num==5:
        print ("Sorry, you lose!")
        break
    cc+=1
else:
    print ("You win!")

#Your own while/else
from random import randint
random_number=randint(1,10)
guesses_left=3

while guesses_left>0:
    guess=int(input("Your guess: "))
    guesses_left -= 1
    if guess == random_number:
        print ("You win!")
        break
        guesses_left += 1
else:
    print ("You lose!")






