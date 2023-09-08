# Encapsulation is the process of data hiding in OOP approach of programming.
# Using this feature we make our attributes private, public or/and protected

# Public Attributes
# These attributes are accessible from both inside the clas and outside the class
class Vehicle:
     engine_type = "Petrol"

     def description(self):
         return f"The vehicle has {self.engine_type} engine"

v = Vehicle()
print(v.engine_type)  # Petrol

# Protected Attributes
# These attributes should be accessible from the same class or the child class only

class Vehicle:
    _colour = "blue"   # Protected member because of the single underscore in the beginning of the variable

    def colour_desc(self):
        print(f"The colour of the vehicle is {self._colour}")

class Bike(Vehicle):
    def colour_desc(self):
        print(f"The colour of the bike is {self._colour}")

b = Bike()
print(b._colour)  # blue. Python is flexible, so it also allows the protected members to be accessible from outside the
                 # class. But, it is not recommended to do so.


# Private Attributes
class Vehicle:
    __colour = "red"  # Private member because of the double underscore in the beginning of the variable

    def colour_desc(self):
        return f"the colour of the vehicle is {self.__colour}"

v = Vehicle()
# print(v.__colour)  # Attribute Error
print(v.colour_desc())

