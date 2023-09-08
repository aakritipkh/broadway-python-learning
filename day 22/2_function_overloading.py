# Function / Method Overloading
# If the function is defined inside a class then the function is called a method. Methods are called using object

# Function overloading is a term used in Programming if the same function definition is repeated multiple times
# Python doesn't support function overloading or method overloading
def addition(a, b):
    return a + b

def addition(a, b, c):
    return a + b + c

# r1 = addition(1, 2)
r2 = addition(2, 3, 4)
# print(r1)
print(r2)

# Even we have defined two addition functions with different number of parameters, but the latest one only
# considered by python

# This problem in python can be solved in a tricky way

def addition(a, b, c=0, **kwargs):
    return a + b + c + sum(kwargs.values())
r1 = addition(2, 3)
r2 = addition(2, 3, 4, p=5, q=6)
print(r2)

class A:
    def test_fxn(self):
        return "Im learning Python"
    def test_fxn(self):
        return "Hello World"

obj = A()
print(obj.test_fxn())  # Hello World

# Like function overloading, method overloading is also not possible in possible
