class Parent(object):                            # Base / Parent / pld / super class
    def override(self):                          # instance method of Parent class
        print("PARENT override() functon")

class Child(Parent):                             # child / Derived / sub class / new class
    def override(self):                          # instance method of Child class
        print("CHILD override() function")

dad = Parent()                                   # creating instance / object of Parent class                 
son = Child()                                    # creating instance / object of child class

dad.override()                                   # calling override () function using instance of parent class           
son.override()                                   # calling override () function using instance of child class