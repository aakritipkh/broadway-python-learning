from estd_connection import estd_connection

cursor = estd_connection()

id = input("Enter student's ID ")

sql = f"""
DELETE FROM STUDENTINFO WHERE ID='{id}'
"""

cursor.execute(sql)
print("Student deleted successfully!!")
