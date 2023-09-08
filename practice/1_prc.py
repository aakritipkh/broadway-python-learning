# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000,
# else return their sum.

num1 = int(input("Input the first number"))
num2 = int(input("Input the second number"))

if num1 * num2 <= 1000:
    product = num1 * num2
    print(f"The product of the given numbers in {product}")

else:
    summation = num1 + num2
    print(f"The summation of given numbers is {summation}")


