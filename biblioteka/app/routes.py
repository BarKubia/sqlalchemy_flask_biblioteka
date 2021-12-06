from app import app
from app.db_helpers import library_database
from datetime import datetime

@app.route("/api/v1/library/", methods=["GET"])
def get_all():
    return library_database.list()

@app.route("/api/v1/library/add_a", methods=["POST"])
def add_author():
    username="J_Rogers"
    email ="J_Rogers@wp.pl"
    name="Jenny"
    surname="Rogers"
    return library_database.add_author(username, email, name, surname)

@app.route("/api/v1/library/add_b", methods=["POST"])
def add_book():
    title="Kuchnia indyjska"
    year = 2001
    return library_database.add_book(title, year)
    
@app.route("/api/v1/library/add_borrow/<int:book_no>", methods=["POST"])
def add_borrowed(book_no):
    who_borrowed = "Tom" 
    when_borrowed = datetime.fromisoformat('2011-11-04')
    when_gave_back = datetime.fromisoformat('2012-11-04')
    return library_database.add_borrowed(who_borrowed , when_borrowed , when_gave_back , book_no)

@app.route("/api/v1/library/update_a/<int:author_no>", methods=["PUT"])
def update_author(author_no):
    username="Dav_Lyn"
    email ="dav_lyn@44.o2"
    name="David"
    surname="Lynch"
    return library_database.update_author(username, email, name, surname, author_no)

@app.route("/api/v1/library/update_b/<int:book_no>", methods=["PUT"])
def update_book(book_no):
    title="O krok od nich"
    year = 2020
    return library_database.update_book(title, year, book_no)

@app.route("/api/v1/library/update_borrow/<int:borrow_no>", methods=["PUT"])
def update_borrowed(borrow_no):
    who_borrowed = "Jack" 
    when_borrowed = datetime.fromisoformat('2021-11-04')
    when_gave_back = datetime.fromisoformat('2022-11-04')
    return library_database.update_borrowed(who_borrowed, when_borrowed, when_gave_back, borrow_no)

@app.route("/api/v1/library/delete_a/<int:author_no>", methods=['DELETE'])
def delete_author(author_no):
    return library_database.delete_author(author_no)

@app.route("/api/v1/library/delete_b/<int:book_no>", methods=['DELETE'])
def delete_book(book_no):
    return library_database.delete_book(book_no)

@app.route("/api/v1/library/delete_borrow/<int:book_no>", methods=['DELETE'])
def delete_borrow(book_no):
    return library_database.delete_borrow(book_no)

@app.route("/api/v1/library/add_association", methods=['POST'])
def add_association():
    author_no=2
    book_no=1
    return library_database.add_association(author_no, book_no)
