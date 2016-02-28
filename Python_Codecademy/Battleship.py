#battleship
board=[]
for i in range(0,5):
    board.append(["0"]*5)
def print_board(board):
    for row in board:
        print (" ".join(row))

#Hide
from random import randint
board=[]
for i in range(0,5):
    board.append(["0"]*5)
def print_board(board):
    for row in board:
        print (" ".join(row))

def random_row(board):
    return randint(0,len(board)-1)
def random_col(board):
    return randint(0,len(board)-1)

ship_row= random_row(board)
ship_col= random_col(board)

guess_row=int(input("Guess Row: "))
guess_col=int(input("Guess Col: "))

print (ship_row)
print (ship_col)

for turn in range(4):
    print ("Turn",turn+1)

if guess_row==ship_row and guess_col==ship_col:
    print ("Congrats!")
else:
    print ("You missed my battleship!")

if guess_row not in range(5) or guess_col not in range(5):
    print ("Oops!")
elif board[guess_row][guess_col]:
    print ("You guessed one that one already")
else:
    print ("You missed my battleship!")


board[guess_row][guess_col]="X"
print (print_board(board))

if turn==3:
    print ("Game Over")





