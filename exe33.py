
i = 0                                        # initializing i
numbers = []                                 # creating empty list

while i < 6 :                                # syntax of while loop
    print(f" At the top i is {i}")
    numbers.append(i)

    i += 1
    print("numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ") 

for num in numbers :
    print(num)