import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="library_db"
    )

    cursor = conn.cursor()

    print("Database Connected Successfully")

except mysql.connector.Error as err:
    print("Error:", err)