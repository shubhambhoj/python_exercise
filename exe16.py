from sys import argv

script, filename = argv

print(f"We're going to erase{filename}.")
print("If you don't want that,hit CTRL-C (^C).")
print("If you do want that,hit RETURN.")

input("?")

print("opening the file...")       
txt = open(filename)            
print(txt.read())               # print the file

target = open(filename,'w')

print("truncating the file. Goodbye!")

# delete lines of the file

target.truncate()               

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# write new lines in file

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it")
target.close()                      # stop writting in the file

# again print the file 

target1 = open(filename)
print(target1.read())