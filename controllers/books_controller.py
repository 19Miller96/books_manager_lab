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
@books_blueprint.route('/books/new')
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors=authors)
# GET '/books/new'

# CREATE
# POST '/books'

# SHOW
# GET '/books/<id>'

# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'

# DELETE
# DELETE '/books/<id>'
