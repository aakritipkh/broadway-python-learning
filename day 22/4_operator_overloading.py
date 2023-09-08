# Operator overloading is the way of defining how an operator behaves in its operation
# For example '+' operator in the integer operator behaves different from the string operation

a = 1
b = 2
print(a + b)  # 3

m1 = "Hello"
m2 = "World"
print(m1 + m2)  # "HelloWorld"

# Such operator functions are defined in the built-in classes of Python. These methods are called magic methods.
# __add__(), __mull()__, __gt__(), __lt__(), __sub__() etc. are the examples of magic methods

a = 1
b = 2
print(a + b)  # 3
print(a.__add__(b))  # 3

