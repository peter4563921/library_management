from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="library_db"
)

cursor = conn.cursor()

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

        sql = """
        INSERT INTO books (title, author, quantity)
        VALUES (%s, %s, %s)
        """

        values = (title, author, quantity)

        cursor.execute(sql, values)
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

        sql = """
        INSERT INTO issued_books
        (student_name, book_name, author_name, quantity)
        VALUES (%s, %s, %s, %s)
        """

        values = (
            student_name,
            book_name,
            author_name,
            quantity
        )

        cursor.execute(sql, values)
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