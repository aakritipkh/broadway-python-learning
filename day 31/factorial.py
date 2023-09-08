# Calculate the factorial of 5 using normal loop, reduce() function and recursive function


# left to write





# reduce()
from functools import reduce
result = reduce(lambda x, y: x*y, range(1, 6))
print(result)


# Recursive function
# If a function call is made from inside the definition of the same function then such a
# function is called a recursive function

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num * 1)
