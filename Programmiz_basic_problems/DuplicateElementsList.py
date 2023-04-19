# replace ___ with your code

# define a list
my_list = [2, "python", 5, 7, "python", "java", 5]

# convert list to set, so that
# unique elements will be selected
my_set = set(my_list)

# empty list to store duplicate elements
repeated_elements = []

# loop through my_set and check if the element
# is occurred more than one time in my_list
for element in my_set:
    if my_list.count(element) > 1:
        repeated_elements.append(element)

# print the duplicate elements
print(repeated_elements)
