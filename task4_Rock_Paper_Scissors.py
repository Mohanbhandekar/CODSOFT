from random import *

r=["Rock","Paper","Scissors"]
comp=0
user=0
while True:
    tie=0
    temp=choice(r)
    print("choose any one :  Rock->1   Paper->2    Scissors->3 ",end="")
    n=int(input())
    if n==1:
        key="Rock"
    elif n==2:
        key="Paper"
    else:
        key="Scissors"
        
    if (temp=="Rock" and key=="Scissors") or (temp=="Scissors" and key=="Paper") or (temp=="Paper" and key=="Rock"):
        print("\n\nYou lose!")
        print("Your choise => ",key,"\nComputer's choise => ",temp)
        comp+=1
    elif (key=="Rock" and temp=="Scissors") or (key=="Scissors" and temp=="Paper") or (key=="Paper" and temp=="Rock"):
        print("\n\nYou win!")
        print("Your choise => ",key,"\nComputer's choise => ",temp)
        user+=1
    else:
        tie=1
        print("\n\nThere's a tie")
        print("Your choise => ",key,"\nComputer's choise => ",temp)

    if tie==0:
        print("press 1 to play one more round else press 2 to terminate ")
        t=int(input())
        if t==1:
            continue
        else:
            print("\n\noverall score \nYour score= ",user,"       computer score = ",comp)
            break
        





