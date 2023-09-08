# Take two numbers as input and add those numbers. Handle the possible execptions

try:
    n1 = int(input("Enter the first number"))
    n2 = int(input("Enter the second number"))
except ValueError:
    print("Please provide a valid number")
except ZeroDivisionError:
    print("Please provide a number other than zero")
else:
    result = n1 + n2
    print(result)

