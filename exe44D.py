class Parent(object):

    def override(self):
        print("PARENT override() function")

    def implicit(self):
        print("PARENT implicit() function")

    def altered(self):
        print("PARENT altered() function.")

class Child(Parent):

    def override(self):
        print("CHILD override() function")

    def implicit(self):
        print("CHILD implicit() function")

    def altered(self):
        print("CHILD,BEFORE PARENT altered() function.")
        super(Child, self).altered()
        print("CHILD,AFTER PARENT altered() function.")  

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()