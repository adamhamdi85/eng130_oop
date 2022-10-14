# create a class called Animal - file-name starts with a - class name starts with A
# add the common attributes/variables/behaviour/functions
# syntax class name: - class Animal:
class Animal:   # follow correct naming convention and best practices
    # initialise the class created with builtin method called __init(self)
    # self refers to current class
    def __init__(self):   # any attributes missing attached to the class should be part of init method
        # self.var = True
        self.alive = True
        self.spine = True
        self.eyes = True

# let's create some methods to add common behaviours
    def breathe(self):
        return "keep breathing to stay alive "
    # let's add one more behaviour
    def eat(self):
        return "time to eat!... "

# create an object of this class
cat = Animal()  # this will create an object of our Animal class
# print(cat.breathe())   # calling method using object method of the Animal class
# print(cat.eat())