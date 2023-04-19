# Replace ___ with your code


# create the class
class Square:
    # define the __init__() method
    def __init__(self, length1):
        self.length1 = length1

    # define the compute_area() method
    def compute_area(self):
        area = self.length1**2
        print(area)

    # define the compute_perimeter() method
    def compute_perimeter(self):
        perimeter = 4 * self.length1
        print(perimeter)


# get integer input
length = int(input())

# create an object of Square
s1 = Square(length)

# call compute_area() and print the area
s1.compute_area()

# call compute_perimeter() and print the perimeter
s1.compute_perimeter()
