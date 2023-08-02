# We can loop through the list in the following way


a = [1, 2, 3, 4]
for i in a:
    print(i)

b = []
for i in a:
    value = i ** 2
    b.append(value)
print(b)

# Recreating the above code using list comprehension
result = [i ** 2 for i in a]
print(result)
