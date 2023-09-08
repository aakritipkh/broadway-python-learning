# Create a class Person with  instance attributes name and age. create method get_details in this cass to print name
# and age.

class Person:
    category = "person"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"The person is {self.name} and is {self.age} years old"



p = Person("John", 20)
print(p.category)
print(p.name)
print(p.age)
print(p.description())
