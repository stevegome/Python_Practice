def find_majority_element(num_list):
    # iterate through each number in the list
    for number in num_list:
        # check the number of occurrence of each element
        count = num_list.count(number)
        # if the number of occurrences is greater than
        # n // 2, where n is the length of the list
        # len(num_list) returns the length of the list
        if count > len(num_list) // 2:
            return number


# given list with majority element
numbers = [1, 2, 1, 3, 9, 1, 1]

# call the method with list as an argument
result = find_majority_element(numbers)
print(result)
