# create tables
CREATE_BOOKS_TABLE = (
    "CREATE TABLE IF NOT EXISTS books (book_title TEXT, book_author TEXT, isbn BIGINT PRIMARY KEY, quantity INTEGER, year INTEGER);"
)

# insert into tables
INSERT_BOOK = "INSERT INTO books (book_title, book_author, isbn, quantity, year) VALUES (%s, %s, %s, %s, %s);"

# view from tables
GET_ALL_BOOKS = "SELECT * FROM books ORDER BY year;"
GET_BOOK = "SELECT * FROM books WHERE isbn = (%s) ORDER BY year;"
GET_BOOK_TITLE_AUTHOR = "SELECT * FROM books WHERE book_title=(%s) OR book_author=(%s) ORDER BY year;"

# update tables
UPDATE_BOOK = "UPDATE books SET book_title=(%s), book_author=(%s), quantity=(%s), year=(%s) WHERE isbn=(%s);"

# delete from tables
DELETE_BOOK = "DELETE FROM books WHERE isbn=(%s);"