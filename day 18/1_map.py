# map()
# map() is a built-in function that takes two parameters as an input. First parameter is function and second parameter
# is an iterable.
# map() function changes every element in an iterable to some other form

nums = [1, 2, 3, 4, 5]
def increase_by_10(data):
    return data + 10

result = map(increase_by_10, nums)
print(nums)
print(list(result))

increase_by_10 = map(lambda x: x + 10, nums)
print(list(increase_by_10))






nums = [1, 2, 3, 4, 5]
def to_the_power_3(data):
    return data ** 3

result = map(to_the_power_3, nums)
print(nums)
print(list(result))

is_even = map(lambda x: x % 2 == 0, nums)
print(list(is_even))


