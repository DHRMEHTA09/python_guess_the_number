import random
from art import logo
import os
should_continue=True


def compare(chosen_number,guessed_number,i):
    if guessed_number==chosen_number:
        return "You Won"
        
    elif guessed_number>chosen_number:
        return "Too high"
    elif guessed_number< chosen_number:
        return "Too low"
         

def difficult(chosen_number):
    k=5
    
    for i in range (6):


        if i==5:
            print(f"you lost,computer scored: {chosen_number}")
            break

        print(f"You have {k} attempts left")
        guessed_number=int(input("Make a Guess: \n"))
        score=compare(chosen_number,guessed_number,i)
        if score=="You Won":
            
            print(f"{score},computer guessed: {chosen_number},You Guessed: {guessed_number}")
            i=6
        
        else:
            print(score)
        k=k-1    
        
def easy(chosen_number):
    k=10
    
    for i in range (11):
        if i==10:
            print(f"you lost,computer scored: {chosen_number}")
            break


        print(f"You have {k} attempts left")
        guessed_number=int(input("Make a Guess: \n"))
        score=compare(chosen_number,guessed_number,i)
        if score=="You Won":
            
            print(f"{score},computer guessed: {chosen_number},You Guessed: {guessed_number}")
            i=11
            break
        
        else:
            print(score)        
        k=k-1


while should_continue:
    print("Welcome to the guess the number game !!!")
    print(logo)
    print("I am thinking a number between 1 to 100.")
    chosen_number=random.randint(1,100)
    result=input("Type 'easy' if you want to play easy level or type 'difficult' to play difficult level.").lower()
    if result=="easy":
        easy(chosen_number)
    elif result=="difficult":
        difficult(chosen_number)
    answer=input("do you want to restart a new game 'yes' or 'no'").lower()
    if answer=="no":
        
        should_continue=False
        os.system('cls')
    else:
        os.system('cls')           
