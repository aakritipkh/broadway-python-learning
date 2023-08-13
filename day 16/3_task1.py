student_list = [("name", "Jon"), ("age", 25), ("address", "KTM")]

# Create dictionary of the above data using dictionary comprehension

student = {key: value for key, value in student_list}
print(student)
