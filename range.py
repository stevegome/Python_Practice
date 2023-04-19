numbers = [10, 45, 61, -6]

# assigning the first value to the largest variable
# we will update the largest variable inside the loop
largest = numbers[0]

# loop iterates from 0 to last item of numbers
for number in numbers:
    if largest < number:
        largest = number

print(f"largest: {largest}")
