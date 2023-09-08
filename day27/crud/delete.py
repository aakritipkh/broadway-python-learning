import json
filename = "students.json"

def delete_student(student_id):
    with open(filename, "r") as fp:
        students = json.loads(fp.read())
        student = list(filter(lambda x: x["id"] == student_id, students))
        if student:
            student = student[0]
            students.remove(student)
            with open(filename, "w") as fw:
                fw.write(json.dumps(students, indent=2))
            print("Student has been removed")

        else:
            print("Invalid ID")




    repeat = input("Do you want to continue?(y/n)")
    return True if repeat.lower() == "y" else False
