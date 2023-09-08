# Create a class Person with  instance attributes name and age. create method get_details in this cass to
# print name and age.
# Create another class Employee with attributes salary and designation and inherits the Person class.
# Create a method get_details in this class to print name, age, salary and designation of the Employee

class Person:
    category = "person"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_details(self):
        return f"The person is {self.name} and is {self.age} years old"

class Employee(Person):

    def __init__(self, name, age, salary, designation):
        super().__init__(name, age)
        self.salary = salary
        self.designation = designation

    def get_details(self):
        print(super().get_details())
        return f"The person earns a {self.salary} and is a {self.designation}"


q = Employee("John", 30, 20000, "Manager")
print(q.get_details())

