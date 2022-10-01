class Parent(object):

    def altered(self):
        #self.a = m
        #print(self.a)
        print("PARENT altered() function")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered() function")
        #super(child, self).altered()
        super().altered()
        print("CHILD, AFTER PARENT altered() function")

dad = Parent()
son = Child()
dad.altered()
son.altered()