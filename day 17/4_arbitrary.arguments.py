# *args and **kwargs are the arbitrary arguments
# These arguments can take dynamic number of parameters
# They are like an expandable bucket

def addition(*args):
    return sum(args)
    # print(type(args))
    # print(args)  #tuple

result = addition(1, 2, 3, 4)
print(result)

def addition(**kwargs):
    return sum(kwargs.values())
    #print(kwargs)
    #print(type(kwargs))  #dict

result = addition(a=1, b=2, c=3, d =4)
print(result)
