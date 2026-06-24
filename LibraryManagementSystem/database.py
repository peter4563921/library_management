import sqlite3

try:
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        quantity INTEGER
    )
    """)

    conn.commit()

    print("Database Connected Successfully")

except Exception as err:
    print("Error:", err)
