'''SNAKE WATER GUN GAME'''
'''IN THIS STEP WE ARE IMPORTING AN INBUILT MODULE RANDOM WHICH WILL HELP US IN RANDOMIZING THE COMPUTERS OUTPUT'''
import random
'''THIS IS A MODULE FOR MAKING GUI'''
import easygui
def game(user,comp):#HERE WE ARE DEFINING A FUNCTION THAT WILL HELP US IN COMPARING THE OUTPUT OF THE USER AND THE COMPUTER AND DECIDE THE WINNER
    if user==comp:
        return None
    elif comp=='s':
        if user=='w':
            return False
        elif user=='g':
            return True    
    elif comp=='w':
        if user=='s':
            return True
        elif user=='g':
            return False
    elif comp=='g':
        if user=='s':
            return False
        elif user=='w':
            return True           #THIS PART IS THE LOGICAL PART
'''NOW WE NEED TO THINK ABOUT THE COMPUTER OUTPUT '''
comp=("Computer's turn : Snake(s) Water(w) Gun(g)")
randno=random.randint(1,3)        #SO AFTER CALLING THE RANDOM FUNCTION WE ARE GRNERATING RANDOM NUMBERS BETWEEEN 1 AND 3  
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
else:
    comp='g'       #ASSIGNED THOSE VALUES TO THE COMPUTERS OUTPUT
#                     '''TAKING INPUT FROM THE USER'''   
print("WELCOME TO THE GAME OF SNAKE WATER AND GUN SNAKE YOU ARE AGAINST COMPUTER \n           MAY THE BETTER PLAYER WIN ") 
user=input("User's turn: Snake(s) Water(w) Gun(g): ")
print(f"Computer chose {comp}")
print(f"user chose {user}")
f=game(user,comp)
if f==None:
   easygui.ynbox('ITS A DRAW !')
elif f:
    easygui.ynbox('YOU WIN COMPUTER NOOBDA')
else:
    easygui.ynbox('YOU LOOSE KOI NA')

