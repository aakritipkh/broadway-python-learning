#wap to delete all the occurences of a specified charactet


# input = a
# output remove the specified letter

s = "All the occurrences of a specified character in given string"
char = input("Enter an alphabet")
result = ""
for each in s:
    if each.lower() == char.lower():
        continue
    result += each
print(result)

