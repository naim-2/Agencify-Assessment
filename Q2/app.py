import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from dbHelper.dbHelper import *
from datetime import datetime
from psycopg2.extras import RealDictCursor

load_dotenv()

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

# add book
@app.route('/add-book', methods=['POST'])
def add_book():
    try:
        title = request.get_json()['title']
        author = request.get_json()['author'] 
        isbn = request.get_json()['isbn']
        quantity = request.get_json()['quantity'] 
        year = request.get_json()['year']

        current_year = datetime.now().year
        if type(quantity) != int or quantity <= 0 or quantity >= 10 ** 4:
            return jsonify({'Error adding book: ': 'Quantity must be an integer between 0 and 10000'}), 400
        if type(year) != int or year <= 867 or year > current_year:
            return jsonify({'Error adding book: ': 'Year should be between 867 and ' + current_year + 1}), 400
        
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(CREATE_BOOKS_TABLE)
                cursor.execute(GET_BOOK, (isbn, ))
                if(cursor.fetchall()==[]):
                    cursor.execute(INSERT_BOOK, (title, author, isbn, quantity, year))
                    return jsonify({'message': 'Book has been added successfully!'})
        return jsonify({'message': 'Book already exists!'})
    except Exception as e:
        return jsonify({'Error adding book: ': str(e)})

# list all books
@app.route('/all-books', methods=['GET'])
def get_books():
    with connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(GET_ALL_BOOKS)
            books = cursor.fetchall()
            return jsonify(books)

# update book
@app.route('/update-book', methods=['PUT'])
def update_book():
    try:
        title = request.get_json()['title']
        author = request.get_json()['author']
        year = request.get_json()['year']
        quantity = request.get_json()['quantity']
        isbn = request.get_json()['isbn']
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(GET_BOOK, (isbn, ))
                if(cursor.fetchall()==[]):
                    return jsonify({'message': 'No such book exists!'})
                cursor.execute(UPDATE_BOOK, (title, author, quantity, year, isbn))
                return jsonify({'message': 'Book has been updated successfully!'})
    except Exception as e:
        return jsonify({'Error updating book: ': str(e)})

# delete book 
@app.route('/delete-book/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_BOOK, (isbn, ))
            if(cursor.fetchall()==[]):
                return jsonify({'message': 'No such book exists!'})
            else:
                cursor.execute(DELETE_BOOK, (isbn, ))
                return jsonify({'message': 'Book has been deleted successfully!'})

# view a book based on author or title
@app.route('/get-book', methods=['GET'])
def get_book():
    title = request.args.get('title')
    author = request.args.get('author')
    books = []
    with connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(GET_BOOK_TITLE_AUTHOR, (title, author))
            books.append(cursor.fetchall())
            print(books)
            if(books==[[]]):
                return jsonify({'message': 'No such book exists!'})
            return jsonify(books)
        
if __name__ == '__main__':
    app.run()