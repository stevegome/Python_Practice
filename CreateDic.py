my_dict = {}

# use for loop to iterate from 1 to 3, including 3
for i in range(1, 4):
    # inside the loop, take input for key and value and store them in my_dict
    key = int(input("Enter integer key : "))
    value = input("Enter string value : ")
    my_dict_new = my_dict.update({key: value})

# print my_dict
print(my_dict)
