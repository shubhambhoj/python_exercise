from sys import exit

def gold_room() :
    print("This room is full of gold.")
    print("Front of you there are three boxes.which one you want to open")
    print("'left', 'center', 'right' and if you don't say 'NO'")
    
    choice = input("> ")
    while (True):
        if choice == 'left' :
            print(f"you opened {choice} , This box is full diamonds.")
            dead("grat choice.")
        elif choice == 'center':
            print(f"you opened {choice} , This box is full rocks.")
            print("Do you want another chance ?? YES or NO")

            chance = input("> ")

            if chance == 'yes' or chance == "YES" :
                print("which box do you want to open ??")
                choice = input("> ")

            else :
                print("sorry,your chance is gone.")
                dead("try again.")   
        else :
            print(f"you opened {choice} , This box is full gold.")
            print("Do you want open another box ?? YES or NO")
            chance = input("> ")
            if chance == 'yes' or chance == "YES" :
                print("which box do you want to open ??")
                choice = input("> ")
            else :
                dead("you say,'No' ")      

def evil_magic():
    print("Here you see the great evil magician.")
    print("he ask you a question.")
    print("Which thing is most important for servive.??")
    print("Your options are 1)hope 2)love 3)family and 4)another thing ")
    
    option = input("> ")
    if option == "hope" :
        print(f"You said, {option} is most important for servive,really??")
        print("You choose wrong option")
        dead("You are killed by evil magician.")

    elif option == "love" :
        print(f"You said, {option} is most important for servive,really??")
        print("You choose wrong option")
        print("Do you want try again?")
        opt = input("> ")
        if opt == "yes":
            evil_magic()
        else :    
            dead("You are killed by evil magician.") 
    
    elif option == "family" :
        print(f"You said, {option} is most important thing for servive")
        print("evil magician is not agrre with you.")
        print("again magician gives you one more chance for being alive.if you give answer of he's question.")
        print("what is important ? 'money' or 'respect'")
        imp = input("> ")

        if imp == "money" :
            print("you are wrong money is not every thing.")
            dead("you are greedy.")
        elif imp == "respect" :
            print("ok , you think respect is important,then you have another test.")
            gold_room()
        else :
            print("you choose wrong.")
            dead("you are loser.")
    
    else :
        print("you choose differ option.")
        print("so, I have test for you.")
        gold_room()


def dead(why):
    print(why,"bye!!")
    exit(0)

def start():
    print("You are in a dark room.")
    print(" There is a door to your right and left.")
    print("which one do you take ?")

    choice = input("> ")

    if choice == "left" :
        gold_room()
    elif choice == "right" :
        evil_magic()
    else :
        dead("You stamble around the room until you starve.")    


start()