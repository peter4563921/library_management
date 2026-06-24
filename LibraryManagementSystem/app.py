from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Database Connection
conn = sqlite3.connect("library.db", check_same_thread=False)
cursor = conn.cursor()

# Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    quantity INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS issued_books (
    issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT,
    book_name TEXT,
    author_name TEXT,
    quantity INTEGER
)
""")

conn.commit()

# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Add Book
@app.route('/addbook', methods=['GET', 'POST'])
def add_book():

    if request.method == 'POST':

        title = request.form['title']
        author = request.form['author']
        quantity = request.form['quantity']

        cursor.execute(
            "INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)",
            (title, author, quantity)
        )

        conn.commit()

        return redirect('/viewbooks')

    return render_template('add_book.html')


# View Books
@app.route('/viewbooks')
def view_books():

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    return render_template('view_books.html', books=books)


# Issue Book
@app.route('/issuebook', methods=['GET', 'POST'])
def issue_book():

    if request.method == 'POST':

        student_name = request.form['student_name']
        book_name = request.form['book_name']
        author_name = request.form['author_name']
        quantity = request.form['quantity']

        cursor.execute(
            """
            INSERT INTO issued_books
            (student_name, book_name, author_name, quantity)
            VALUES (?, ?, ?, ?)
            """,
            (
                student_name,
                book_name,
                author_name,
                quantity
            )
        )

        conn.commit()

        return redirect('/viewissuedbooks')

    return render_template('issue_book.html')


# View Issued Books
@app.route('/viewissuedbooks')

def view_issued_books():

    cursor.execute("SELECT * FROM issued_books")
    books = cursor.fetchall()

    return render_template(
        'view_issued_books.html',
        books=books
    )


if __name__ == '__main__':
    app.run(debug=True)
