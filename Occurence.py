# Replace ___ with your code

# take string input for string1
string1 = input()

# take character input for character1
character = input()

count = 0

# use for loop to iterate through string1
for string in string1:
    # check if character is present in the string or not
    if string == character:
        count = count + 1

print(count)
