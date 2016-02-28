#Conditionals & Control
def clinic():
    print ("You've just entered the clinic!")
    print ("Do you take the door on the left or right?")
    answer = input("Type left or right and hit 'Enter'.").lower
    if answer == "left" or answer == "l":
        print ("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right" or answer == "r":
        print ("Of course this is the Argument Room, I've told you that already!")
    else:
        print ("You didn't pick left or right! Try again.")
clinic()


response = "Y"
answer = "Left"
if answer == "Left":
    print (response)

def using_control_once():
    if 1<2:
        return "Success #1"

def using_control_again():
    if 2<3:
        return "Success #2"
print (using_control_once)
print (using_control_again)


def greater_less_equal_5(answer):
    if answer>5:
        return 1
    elif answer<5:          
        return -1
    else:
        return 0
        
print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))r
