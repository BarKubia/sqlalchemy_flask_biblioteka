from app import app
from app.db_helpers import library_database
from datetime import datetime
import json

@app.route("/api/v1/library/", methods=["GET"])
def get_all():
    library_database.list()
    return "200"

@app.route("/api/v1/library/add_a/<username>/<email>/<name>/<surname>", methods=["POST"])
def add_author(username,email,name,surname):
    library_database.add_author(username, email, name, surname)
    return "200"

@app.route("/api/v1/library/add_b/<title>/<int:year>", methods=["POST"])
def add_book(title,year):
    library_database.add_book(title, year)
    return "200"
    
@app.route("/api/v1/library/add_borrow/<int:book_no>/<who_borrowed>/<when_borrowed_l>/<when_gave_back_l>", methods=["POST"])
def add_borrowed(book_no,who_borrowed,when_borrowed_l,when_gave_back_l):
    when_borrowed = datetime.fromisoformat(when_borrowed_l)
    when_gave_back = datetime.fromisoformat(when_gave_back_l)
    library_database.add_borrowed(who_borrowed , when_borrowed , when_gave_back , book_no)
    return "200"

@app.route("/api/v1/library/update_a/<int:author_no>/<username>/<email>/<name>/<surname>", methods=["PUT"])
def update_author(author_no,username,email,name,surname):
    library_database.update_author(username, email, name, surname, author_no)
    return "200"

@app.route("/api/v1/library/update_b/<int:book_no>/<title>/<int:year>", methods=["PUT"])
def update_book(book_no,title,year):
    library_database.update_book(title, year, book_no)
    return "200"

@app.route("/api/v1/library/update_borrow/<int:borrow_no>/<who_borrowed>/<when_borrowed_l>/<when_gave_back_l>", methods=["PUT"])
def update_borrowed(borrow_no,who_borrowed,when_borrowed_l,when_gave_back_l):
    when_borrowed = datetime.fromisoformat(when_borrowed_l)
    when_gave_back = datetime.fromisoformat(when_gave_back_l)
    # when_borrowed = datetime.fromisoformat('2021-11-04')
    # when_gave_back = datetime.fromisoformat('2022-11-04')
    library_database.update_borrowed(who_borrowed, when_borrowed, when_gave_back, borrow_no)
    return "200"

@app.route("/api/v1/library/delete_a/<int:author_no>", methods=['DELETE'])
def delete_author(author_no):
    library_database.delete_author(author_no)
    return "200"

@app.route("/api/v1/library/delete_b/<int:book_no>", methods=['DELETE'])
def delete_book(book_no):
    library_database.delete_book(book_no)
    return "200"

@app.route("/api/v1/library/delete_borrow/<int:book_no>", methods=['DELETE'])
def delete_borrow(book_no):
    library_database.delete_borrow(book_no)
    return "200"

@app.route("/api/v1/library/add_association/<int:author_no>/<int:book_no>", methods=['POST'])
def add_association(author_no,book_no):
    library_database.add_association(author_no, book_no)
    return "200"
