# Method overriding is possible if one class inherits another class
# In such case child class can override the method of the parent class

class A:
    def message(self):
        return "Hello World"

class B(A):
    def message(self):
        return "Im learning Python"

b = B()
print(b.message())  #

# message() method id defined both in parent and child classes. Here the child class has overriden
# the message() method that is already defined
