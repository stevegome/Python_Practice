# create the person class
class Person:
    # create the greet() method
    def __init__(self, message):
        self.message = message

    def greet(self):
        print(self.message)


# get user input
greeting = input()

# create object
person1 = Person()

# call the greet() method using person1
# use greeting as an argument
person1.greet(greeting)
