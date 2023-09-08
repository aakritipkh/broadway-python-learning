def estd_connection():
    import psycopg2
    conn = psycopg2.connect(
        database="studentdb",
        user="postgres",
        password="nepal",
        host="127.0.01",
        port=5432

    )
    conn.autocommit = True
    print("Connection established successfully !!")
    cursor = conn.cursor()
    return cursor

if __name__ == "__main__":
    estd_connection()
