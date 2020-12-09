from flask import Flask, render_template, request, redirect
from repositories import author_repository
from repositories import book_repository
from models.author import Author
from models.book import Book

from flask import Blueprint
books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/books')
def books():
    # get all the tasks from the DB using the repository functions 
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

# NEW
# GET '/books/new'
@books_blueprint.route('/books/new')
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors=authors)

# CREATE
# POST '/books'

@books_blueprint.route('/books', methods=['POST'])
def create_book():
    # Gather all the data from the form
    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']
    author = request.form['author']

    author = author_repository.select(author_id)
    book = Book(title, genre, publisher, author)
    book_repository.save(book)
    return redirect('/books')

# SHOW
# GET '/books/<id>'

# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'

# DELETE
# DELETE '/books/<id>'
