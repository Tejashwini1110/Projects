#Snake-Water-Gun Game
import random
computer=random.choice([1,-1,0])
youstr=input("Enter your choice:")
youDict={'s':1,'w':-1,'g':0}
reverseDict={1:'Snake',-1:'Water',0:'Gun'}
you=youDict[youstr]

print(f"you chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")

if(computer==you):
    print("Its's a draw")
else:#Method1
    if(computer==-1 and you==0):    #[computer-you]==-1
        print("You lose!")
    elif(computer==-1 and you==1):  #[computer-you]==-2
        print("You win!")
    elif(computer==1 and you==0):   #[computer-you]==1
        print("You win!")
    elif(computer==1 and you==-1):  #[computer-you]==2
        print("You lose!")
    elif(computer==0 and you==1):   #[computer-you]==-1
        print("You lose!")
    elif(computer==0 and you==-1):  #[computer-you]==1
        print("You win!")
    else:
        print("Something went wrong!")


    #Method2(This logic is written on the basis of [computer-you] value)
    """
    if([computer-you]==1 or [computer-you]==-2):
        print("you win")
    else:
        print("you lose")
    """