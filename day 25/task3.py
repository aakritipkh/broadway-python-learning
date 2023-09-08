# Create a dictionary student with keys id, name, age,
# department.Take am input from the user, which
# info(id, name, age or department) he wants to access
# and print the result. Handle the possible exceptions


student = {"id": 10, "name": "John", "age": 20, "department": "Science"}

try:
    key = input("Enter the key you want to access: id, name, age or department")
    data = student[key]
    print(f"The {key} of the student is {data}")
except KeyError:
    print("Please provide a valid key")
