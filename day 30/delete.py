from estd_connection import estd_connection

def delete_student(student_id):
    cursor = estd_connection()


    sql = f"""
    DELETE FROM STUDENTINFO WHERE ID='{id}'
    """

    cursor.execute(sql)
    print("Student deleted successfully!!")



    repeat = input("Do you want to continue?(y/n)")
    return True if repeat.lower() == "y" else False
