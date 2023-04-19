# replace ___ with your code
import math


# function to find the sum of smallest and largest element
# def calc_sum_without_sorting(num_list):
#     # find the smallest and largest value
#     smallest_value = min(num_list)
#     largest_value = max(num_list)
#
#     # find the sum of the smallest and largest elements
#     total = smallest_value + largest_value
#
#     # return the total
#     return total


def calculate_sum_with_sorting(num_list):
    sorted_list = sorted(num_list)
    newsmallest_value = sorted_list[0]
    newlargest_value = sorted_list[len(sorted_list) - 1]

    total = newsmallest_value + newlargest_value
    return total


# list of numbers
numbers = [5, 6, 3, 8, 9]


result = calculate_sum_with_sorting(numbers)

# print the sum
print(result)
