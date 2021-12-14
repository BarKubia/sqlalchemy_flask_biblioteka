from app.models import Author, Book, Borrowed
from app import db
import json


class LibraryDatabase:

    def list(self):
        authors=Author.query.all()
        books=Book.query.all()
        borrows=Borrowed.query.all()

    def add_author(self, username, email, name, surname):
        a=Author(username=username,email=email,name=name,surname=surname)
        db.session.add(a)
        db.session.commit()

    def add_book(self, title, year):
        b=Book(title = title, year = year)
        db.session.add(b)
        db.session.commit()
    
    def add_borrowed(self, who_borrowed, when_borrowed, when_gave_back, book):
        b=Book.query.get(book)
        borrow=Borrowed(who_borrowed = who_borrowed, when_borrowed = when_borrowed, when_gave_back = when_gave_back, books=b)
        db.session.add(borrow)
        db.session.commit()    
 
    def update_author(self, username, email, name, surname, author_no):
        author = Author.query.get(author_no)
        author.username = username
        author.email = email
        author.name= name
        author.surname=surname
        db.session.add(author)
        db.session.commit()

    def update_book(self, title, year, book_no):
        book = Book.query.get(book_no)
        book.title = title
        book.year = year
        db.session.add(book)
        db.session.commit()

    def update_borrowed(self, who_borrowed, when_borrowed, when_gave_back, borrow_no):
        borrow = Borrowed.query.get(borrow_no)
        borrow.who_borrowed = who_borrowed
        borrow.when_borrowed= when_borrowed
        borrow.when_gave_back= when_gave_back
        db.session.add(borrow)
        db.session.commit()

    def delete_author(self, author_no):
        author=Author.query.get(author_no)
        db.session.delete(author)
        db.session.commit()

    def delete_book(self, book_no):
        book=Book.query.get(book_no)
        db.session.delete(book)
        db.session.commit()

    def delete_borrow(self, borrow_no):
        #b=Book.query.get(book_no)
        borrow = Borrowed.query.get(borrow_no)
        db.session.delete(borrow)
        db.session.commit()

    def add_association(self, author_no, book_no):
        a=Author.query.get(author_no)
        b=Book.query.get(book_no)
        a.books.append(b)
        db.session.add(a)
        db.session.commit()

library_database = LibraryDatabase()