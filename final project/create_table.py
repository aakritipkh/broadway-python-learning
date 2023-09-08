from estd_connection import estd_connection
cursor = estd_connection()

sql = """
CREATE TABLE STUDENTDATA(
    FIRST_NAME CHAR(20),
    LAST_NAME CHAR(20),
    TITLE CHAR(10),
    AGE INT,
    NATIONALITY CHAR(20),
    NUM_COURSES INT,
    NUM_SEMESTER INT, 
    REGISTRATION_STATUS CHAR(20)
)
"""

cursor.execute(sql)
print("Table Created Successfully!")
