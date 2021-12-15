from app import app
from app.db_helpers import library_database
from datetime import datetime
from flask import Response
import json

@app.route("/api/v1/library", methods=["GET"])
def get_all():
    books = library_database.list()
    books_no=len(books)
    books_and_authors={}
    for i in range(0,books_no):
        book=books[i].title
        authors_no=len(books[i].authors)
        if authors_no!=0:
            author=[]
            for n in range(0,authors_no):
                author.append(books[i].authors[n].surname)
        else:
            author=[]
        books_and_authors[book]=author
    books_json=json.dumps(books_and_authors)
    return books_json

"""
@app.route("/api/v1/library", methods=["GET"])
def get_all():
    books_and_authors = {}
    books = library_database.list()
    for book in books:
        if book.authors:
            authors=[]
            for author in authors:
                authors.append(author.surname)
        books_and_authors[book.title]=author
    return json.dumps(books_and_authors)

"""
    

@app.route("/api/v1/library/add_a/<username>/<email>/<name>/<surname>", methods=["POST"])
def add_author(username,email,name,surname):
    library_database.add_author(username, email, name, surname)
    return Response(status=200)

@app.route("/api/v1/library/add_b/<title>/<int:year>", methods=["POST"])
def add_book(title,year):
    library_database.add_book(title, year)
    return Response(status=200)
    
@app.route("/api/v1/library/add_borrow/<int:book_no>/<who_borrowed>/<when_borrowed_l>/<when_gave_back_l>", methods=["POST"])
def add_borrowed(book_no,who_borrowed,when_borrowed_l,when_gave_back_l):
    when_borrowed = datetime.fromisoformat(when_borrowed_l)
    when_gave_back = datetime.fromisoformat(when_gave_back_l)
    library_database.add_borrowed(who_borrowed , when_borrowed , when_gave_back , book_no)
    return Response(status=200)

@app.route("/api/v1/library/update_a/<int:author_no>/<username>/<email>/<name>/<surname>", methods=["PUT"])
def update_author(author_no,username,email,name,surname):
    library_database.update_author(username, email, name, surname, author_no)
    return Response(status=200)

@app.route("/api/v1/library/update_b/<int:book_no>/<title>/<int:year>", methods=["PUT"])
def update_book(book_no,title,year):
    library_database.update_book(title, year, book_no)
    return Response(status=200)

@app.route("/api/v1/library/update_borrow/<int:borrow_no>/<who_borrowed>/<when_borrowed_l>/<when_gave_back_l>", methods=["PUT"])
def update_borrowed(borrow_no,who_borrowed,when_borrowed_l,when_gave_back_l):
    when_borrowed = datetime.fromisoformat(when_borrowed_l)
    when_gave_back = datetime.fromisoformat(when_gave_back_l)
    library_database.update_borrowed(who_borrowed, when_borrowed, when_gave_back, borrow_no)
    return Response(status=200)

@app.route("/api/v1/library/delete_a/<int:author_no>", methods=['DELETE'])
def delete_author(author_no):
    library_database.delete_author(author_no)
    return Response(status=200)

@app.route("/api/v1/library/delete_b/<int:book_no>", methods=['DELETE'])
def delete_book(book_no):
    library_database.delete_book(book_no)
    return Response(status=200)

@app.route("/api/v1/library/delete_borrow/<int:borrow_no>", methods=['DELETE'])
def delete_borrow(borrow_no):
    library_database.delete_borrow(borrow_no)
    return Response(status=200)

@app.route("/api/v1/library/add_association/<int:author_no>/<int:book_no>", methods=['POST'])
def add_association(author_no,book_no):
    library_database.add_association(author_no, book_no)
    return Response(status=200)
