# Python Statement

# Backslash can be used to take a statement to the next line
message = "hello i'm learning" \
          "python"

import json,\
    csv

# We can use ';' to write multiple statements in a same line
name = "Jon"; age = 25

# Indentation in Python is very important.
# An indentation/tab is equivalent in 4 spaces
# We do not use curly braces in python to determine a block of code. Instead, we use indentation.

# Following is an example of a C code
# if (a==2){
# printf("Hello Word")
# }
# Here the block of if condition is determined using curly braces
# But in python block is determined by indentation
# For example
a = 2
if a == 2:
    print("Hello World")
    b = 2
    if b == 2:
        print("Python")
        print("Is")
        print("awesome")
        print("Another Message")
    print("Sth")


# Docstring Example
    message = """
    Python is a high level language.
    It is easy to learn.
    """
    print(message)

    message = "I'm learning python"
    msg = 'he said, "Hello!"'

    # Escape Sequence
    message = 'I\'m learning python'
