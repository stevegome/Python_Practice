# Replace ___ with your code

# import math module

import math

number = int(input("Enter the Number : "))

# use sqrt() to find the square root of the number
new_number = math.sqrt(number)

# get remainder of the square root by using % with 1
remainder = new_number % 1

# if the remainder is equal to 0, print "Perfect Square" Else print "Not a Perfect Square"
if remainder == 0:
    print("Perfect Square")
else:
    print("Not a Perfect Square")
