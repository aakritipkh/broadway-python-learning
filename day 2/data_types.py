### Mutable and Immutable Objects ###
"""
If an object once created can be changed later then the object is a mutable object

But if an object once created can never be changed throughout its life cycle then it is an immutable object.

List, dictionary, set are the example of Mutable objects.
Numbers, Tuple, Boolean, String are the example of Immutable object.
"""

a = ['a', 'b', 'c']
a[1] = 'd'
a

b = (1, 2, 3)
b[1] = 5  # It raises error because theyre immutable object.
