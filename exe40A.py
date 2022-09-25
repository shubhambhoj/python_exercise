'''
# Example of dict.
# access dict 
mystuff = {'apple' : "I AM APPLES!"}
# print(mystuff['apple'])

# use  exe40A module to run
# access function
def apple():
    print("I AM APPLES!")
# Access variable
tangerine = "Living reflection of a dream"
'''
# CLASS EXAMPLE

class Mystuff(object):
    def __init__(self):
        self.tangerine = "and now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

thing = Mystuff()         
thing.apple()
print(thing.tangerine)

