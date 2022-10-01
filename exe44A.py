class Parent(object):                           # Base / Parent / pld / super class
    def implicit(self):                         # instance method of Parent class
        print("PARENT implicit() function")

class Child(Parent):                            # child / Derived / sub class / new class
    pass


dad = Parent()                            # creating instance / object of Parent class
son = Child()                             # creating instance / object Child class

dad.implicit()                            # calling implicit() function using instance of parent class
son.implicit()                            # calling implicit() function using instance of Child class