# Replace ___ with your code

my_dict = {"a": "juice", "b": "grill", "c": "corn"}

# take user input for data
data = input("Enter String input :  ")

# create a flag variable and set it to False
flag = False

# loop through my_dict
for value in my_dict.values():
    # check if the value entered by the user is in the dictionary or not
    # if yes, set flag to True and terminate the loop
    if data in my_dict.values():
        flag = True
        break

# print value found not found based on the flag status
if flag:
    print("Value found")
else:
    print("Value not found")
