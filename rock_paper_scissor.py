import random
import sys
c1=0
c2=0
def game():
    global c1,c2 #tells the program to use the given global variables
    dict1={"scissor":"rock","rock":"paper","paper":"scissor"}
    if userchoice==compchoice:
        c1+=1
        c2+=1
        print("It's a tie !")
    elif dict1[userchoice]==compchoice:
        c2+=1
        print("Uh-Oh, You lose!")
        
    else:
        c1+=1
        print("Yay,you win!")
       
options=["rock","paper","scissor"]
print("WELCOME TO ROCK PAPER SCISSOR GAME!")
print("type 'exit' to exit the game") 
while True:
    userchoice=input("enter rock/paper/scissor: ").lower()
    if userchoice=="exit":
        print("THANKS FOR PLAYING!")
        print("Your Score= ", c1)
        print("Computer's Score= ",c2)
        if(c2>c1):
            print("Winner= Computer")
        elif(c1>c2):
            print("Winner= You")
        else:
            print("Its a tie between you and the computer")
        sys.exit() #exits the program
    if userchoice not in options:
        print("invalid choice, please try again")
        continue # starts over the loop and asks again
           
    compchoice=random.choice(options)
    print(f"computer chooses: {compchoice}")

    game()

       

    
