# creating different type of lists
the_count = [1, 2, 3, 4, 5]
fruits = ['apples','oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# using for loop accessing and printing elements of the following lists.
for number in the_count :
    print(f"This is count {number}")

for fruit in fruits :
    print(f"A fruit of type: {fruit}")

for i in change :
    print(f"I got {i}")

# creating empty list.
elements = []

# using range() in for loop printing number
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # using append() method we can add elements to the end of the list.
    elements.append(i)
# printing elements of elements list.
for i in elements :
    print(f"Element was: {i}")