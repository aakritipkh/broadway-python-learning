# "Python + is + an + awesome + language" split the given string to get a list and join to get another string
# "Python is an awesome language"

a = "Python + is + an + awesome + language"
result = a.split(" + ")
print(result)
a = " ".join(result)
print(a)


