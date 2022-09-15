ani = ['bear','tiger','penguin','zebra','lion','panther','wolf']

# list of ani
print(ani)              #  list
print(ani[1])           #  print index 1 of ani list
print(ani[1][0])        #  print 0th position of index 1 of ani list
print(ani[2])           # o/p = penguin
print(ani[6])           # o/p = wolf
print(ani[5])           # o/p = panther
print(ani[3])           # o/p = zebra
print("*******************")

# USING FOR LOOP ACCESSING ELEMENTS OF LIST
# 1) with out index :

for i in ani :
    print(i)
print()
# 2) with index :    

n = len(ani)
for i in range(n):
    print(f"index {i}: ",ani[i])
print()

# USING WHILE LOOP ACCESSING ELEMENTS OF LIST

n = len(ani)
i = 0 
while i < n :
    print(f"index {i}: ",ani[i])
    i +=1
print()    