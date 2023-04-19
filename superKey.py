# Replace ___ with your code


# create the Animal class
class Animal:
    def eat(self):
        print("I can eat food")


# create the Dog class
class Dog(Animal):
    def bark(self):
        print("I can bark")

    def eat(self):
        super().eat()


# create an object of the Dog class
d1 = Dog()

# call the eat() method using the object
d1.bark()
d1.eat()
