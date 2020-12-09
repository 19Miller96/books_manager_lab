from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository


author_1 = Author("Dan", "Brown")
author_repository.save(author_1)


author_2 = Author("J.K.", "Rowling")
author_repository.save(author_2)


book_1 = Book("davinci-code", "mystery", "penguin", author_1)
book_repository.save(book_1) 