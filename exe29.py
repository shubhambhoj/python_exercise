# people = 20
# cats = 30
# dogs = 15

# getting input from user
people = int(input("Enter number of people: "))
cats = int(input("Enter number of cats: "))
dogs = int(input("Enter number of dogs: "))

if people < cats :
    print("too many cats! The world is doomed!")

if people > cats :
    print("Not many cats! The world is saved!")

if people < dogs :
    print("The world is drooled on!")    

if people > dogs :
    print("The world is dry!")

dogs += 5

if people >= dogs :
    print("people are greater than or equal to dogs.")

if people <= dogs :
    print("people are less than or equal to dogs.")

if people == dogs :
    print("people are dogs.")