# Replace ___ with your code

number = int(input("Enter some no : "))

flag = 0

# create a for loop that runs from 2 to number, not including number
for i in range(2, number):
    # check if number is divisible by any number between 2 to number - 1
    # If yes, set flag to 1
    if number % i == 0:
        flag = 1

# print "Not a Prime Number" if flag is equal to 1, else print "Prime Number"
if flag == 1:
    print("Not a Prime Number")
else:
    print("Prime Number")
