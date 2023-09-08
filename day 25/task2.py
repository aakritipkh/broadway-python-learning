# Take two numbers input and divide a number by another number. Handle the possible exceptions.


try:
    n1 = int(input("Enter a number "))
    n2 = int(input("Enter a number "))
    result = n1 / n2
    print(result)
except ValueError:
    print("Please provide a valid number")
except ZeroDivisionError:
    print("Please provide a number other than zero")
