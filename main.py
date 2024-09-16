import random
while True:
    computer=random.choice([-1,0,1])
    youstr=input("Enter Rock,Scissors,Paper or exit:").lower()
    if(youstr=="exit"):
       print("Exiting....")
       break
    youdict = {"rock":-1,"scissors":0,"paper":1}
    revdict = {-1:"rock",0:"scissors",1:"paper"}
    you=youdict[youstr]
    print(f"you={revdict[you]} \n computer={revdict[computer]}")
    if(computer==you):
        print("Draw")
    else:
        if((you-computer)==2 or (you-computer==-1)):
            print("You Win")
        else:
            print("You lose")    

    # if(you==1 and computer==0):
    #     print("you lose")
    # elif(you==1 and computer==-1):
    #     print("you win")    
    # elif(you==-1 and computer==0):
    #     print("you win")  
    # elif(you==-1 and computer==1):
    #     print("you lose")       
    # elif(you==0 and computer==-1):
    #     print("you lose")   
    # elif(you==0 and computer==1):
    #     print("you win")   
    # else:
    #     print("Error")