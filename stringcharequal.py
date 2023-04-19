# Replace ___ with your code

# take string input for check
check = list((input("Enter a list of no")))

print(f"Length of check is : {len(check)}")


if check[0] == check[len(check) - 1]:
    print("Equal")
else:
    print("Not Equal")
