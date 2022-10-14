class Parent(object):

    def altered(self):
    
        print("PARENT altered() function")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered() function")
        #super(child, self).altered()               # it compelsory in python 2 to give arg.in super()
        super().altered()                           # in python3 it is optional so if we not it take default arg.
        print("CHILD, AFTER PARENT altered() function")

dad = Parent()
son = Child()

dad.altered()
son.altered()