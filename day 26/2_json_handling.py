# JSON stands for JavaScript Object Notation
# It is one of the file formats to transfer data around the web or other system
# It is a very famous way of file transfer in the REST APIs
# Python has a built-in support for json handling

# Rules in a json file
# 1. Keys and values must be enclosed in double quotes
# 2. Information can be enclosed in an array
# 3. Double quotes are not required for the number datatype
# 4. Extension of the json file is .json

# for example:
student = {"name": "Jon", "address": "KTM"}  # This can be a valid JSON
student = {'name': 'Jon', 'address': 'KTM'}  # Invalid JSON. JSON must have double quotes

students = [
    {"name": "Jon", "address": "KTM", "phone": 84843939},
    {"name": "Jane", "address": "BKT", "phone": 28488482},
    {"name": "Harry", "address": "PKR", "phone":  98388848}
]  # Valid JSON


import json

filename = "students.json"
with open(filename, "w+") as fp:
    data = json.dumps(students, indent=2)
    fp.write(data)
    fp.seek(0)
    data = json.loads(fp.read())

name = data[0]["name"]
print(name)

