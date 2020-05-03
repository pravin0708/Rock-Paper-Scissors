import random


def welcome():
    input("Press Y key to start:")

def mainmenu():
    print("1.Rock Paper Scissors\n2.Exit")
    ch=int(input("Enter your choice number:"))
    if ch==1:
        rockpaperscissorsmenu()
    elif ch==2:
        exit()
    else:
        print("Invalid choice!")
        mainmenu()

def rockpaperscissorsmenu():
    print("\n")
    print("1.Play\n2.Return to Main menu")
    ch = int(input("Enter your choice number:"))
    if ch == 1:
        rockpaperscissors()
    elif ch == 2:
        mainmenu()
    else:
        print("Invalid choice!")
        rockpaperscissorsmenu()

def rockpaperscissors():
    print("\n")
    print("**********************************************************************")
    print("WELCOME TO ROCK PAPER AND SCISSORS GAME")
    print("You will be competing against the computer. The player that scores 5 points first, will be declared as the winner!")
    print("If your choice is Rock,please Enter 0")
    print("If your choice is Paper,please Enter 1")
    print("If your choice is Scissors,please Enter 2")
    print("If you wish to exit,please Enter -1")
    print("***********************************************************************")
    uname=input("Enter Your Name:")
    user=0
    comp=0
    cnt=0
    chc=["Rock","Paper","Scissors"]
    while(user<3 and comp<3 and cnt<10):
        cnt+=1
        print("\n"*1)
        u_ch=int(input("Enter your choice:"))
        print("***************************************")
        if u_ch==-1:
            print("Thank you")
            return
        c_ch=random.choice([0,1,2])
        if u_ch==0 and c_ch==1:
            comp+=1
        elif u_ch==0 and c_ch==2:
            user+=1
        elif u_ch==1 and c_ch==0:
            user+=1
        elif u_ch==1 and c_ch==2:
            comp+=1
        elif u_ch==2 and c_ch==0:
            comp+=1
        elif u_ch==2 and c_ch==1:
            user+=1
        print("You:",chc[u_ch])
        print("Computer",chc[c_ch])
        print("\n")
        print(uname.title()+" score:",user,"\t Computer's Score:",comp)
        print("*****************************************")
    if(user>comp):
        print("\n")
        print("*****************************************")
        print("Congragulations!"+" "+uname.title()+" "+"you win!")
        print("\n")
    elif(comp>user):
        print("\n")
        print("*****************************************")
        print("Oops!Sorry you lose. Better luck next time!")
        print("\n")
    else:
        print("\n")
        print("*****************************************")
        print("Match Draw")
        print("\n")
    mainmenu()

welcome()
print("\n")
mainmenu()
