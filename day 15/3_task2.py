n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))
n3 = int(input("Enter the third number"))
if n1 > n2 and n1 > n3:
    print(f"The first number {n1} is the greatest")
elif n2 > n1 and n2 > n3:
    print(f"The second number {n2} is the greatest")
else:
    print(f"The third number {n3} is the greatest")
