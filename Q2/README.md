# Book Library API

## Overview

This API allows you to add, list, update and delete book records.

## Prerequisites

Python 3.7+, Python package manager

# Installation

1. Ensure you are in Q2 folder.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask server to test the endpoints:

```bash
python app.py
```

## Endpoints

1. Add a Book - /add-book (POST)
   This endpoint adds a new book record to the existing database by providing the book's title, author, ISBN, quantity, and year of publication.

### For example:

```json
{
  "title": "The 7 Habits of Highly Effective People",
  "author": "Stephen R. Covey",
  "isbn": "9780743269513",
  "quantity": 20,
  "year": 1989
}
```

#

### Response 1 (book doesn't exist):

```json
{
  "message": "Book has been added successfully!"
}
```

#

### Response 2 (if book already exists):

```json
{
  "message": "Book already exists!"
}
```

2. Get All Books - /all-books (GET)
   This endpoint retrieves records of all books in the database. Example of response received:

```json
[
  {
    "book_author": "Stephen R. Covey",
    "book_title": "The 7 Habits of Highly Effective People",
    "isbn": 9780743269513,
    "quantity": 20,
    "year": 1989
  },
  {
    "book_author": "Dalai Lama and Howard Cutler",
    "book_title": "The Art of Happiness",
    "isbn": 9781573227544,
    "quantity": 14,
    "year": 1998
  }
]
```

#

3. Update a Book - /update-book (PUT)
   This endpoint updates the details of an existing book record by specifying its title, author, ISBN, quantity, and year of publication. For example:

```json
{
  "author": "Dalai Lama and Howard Cutler",
  "title": "The Art of Happiness",
  "isbn": 9781573227544,
  "quantity": 44,
  "year": 1998
}
```

### Response:

```json
{
  "message": "Book has been updated successfully!"
}
```

#

4. Delete a Book - /delete-book/{isbn} (DELETE)
   This endpoint deletes a book from the database by providing its ISBN. For example: {server-link}/delete-book/9780743269513
   ### Response:

```json
{
  "message": "Book has been deleted successfully!"
}
```

#

5. Retrieve a Book - /get-book (GET)
   This endpoint retrieves book details by providing its title, author, or both. For example:
   #
   i. Get book by title: /get-book?title=The Art of Happiness
   #
   ii. Get book by author: /get-book?author=Dalai Lama and Howard Cutler
   #
   iii. Get book by both title and author: /get-book?title=The Art of Happiness&author=Dalai Lama and Howard Cutler

### Response 1 (book found):

```json
[
  [
    {
      "book_author": "Dalai Lama and Howard Cutler",
      "book_title": "The Art of Happiness",
      "isbn": 9781573227544,
      "quantity": 44,
      "year": 1998
    }
  ]
]
```

### Response 2 (book not found)

```json
{
  "message": "No such book exists!"
}
```
