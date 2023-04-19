# Replace ___ with your code


def calculate_factorial(n):
    if n != 1:
        # call calculate_factorial() with appropriate argument
        return n * calculate_factorial(n - 1)

    return n


number = int(input())
result = calculate_factorial(number)
print(result)
