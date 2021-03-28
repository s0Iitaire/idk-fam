# imports random function 
import random

# creates da while loop

game=True
while game == True:
    usersSelect = int(input("choose one of these options:\n 1 = Rock \n 2 = Paper \n 3 = Scissors\n"))
    computerSelect = random.randint(1,3)
    if computerSelect == 1:
        print("computer chose Rock")
    elif computerSelect == 2:
        print("computer chose Paper")
    else:
        print("computer chose scissors")
    if usersSelect == computerSelect:
        print("it'z a draw!")
    elif usersSelect == 1 and computerSelect == 3:
        print("you win!")
    elif usersSelect == 2 and computerSelect == 1:
        print("you win!")
    elif usersSelect == 3 and computerSelect == 2:
        print("you win!")
    else:
        print("computer wins!")
    text = input("play again?")
    if text=="Y":
        game=False
