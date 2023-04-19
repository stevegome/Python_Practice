# replace ___ with your code


# define a function that counts alphabets,
# digits and symbols in a string
def counter(string):
    # initialize the counters
    alphabets = 0
    digits = 0
    symbols = 0

    # loop through the string
    for char in string:
        # check if the character is the alphabet
        # if yes, increment the alphabet counter
        if char.isalpha():
            alphabets = alphabets + 1

        # check if the character is the digit
        # if yes, increment the digit counter
        elif char.isdigit():
            digits = digits + 1

        # check if the character is the symbol
        # if yes, increment the symbol counter
        else:
            symbols = symbols + 1

    # print the results
    print(f"Alphabets: {alphabets}")
    print(f"Digits: {digits}")
    print(f"Symbols: {symbols}")


# call the function
counter("Hello123.")
