# Replace ___ with your code

# get three sides of the triangle from the user
# store them in variables a, b and c
a = int(input())
b = int(input())
c = int(input())

# compute semiperimeter s
s = (a + b + c) / 2
print(s)

# compute area and print it
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(area)
