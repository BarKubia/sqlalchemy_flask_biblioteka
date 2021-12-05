from app import db


association_table = db.Table('association', db.Model.metadata,
    db.Column('author_id', db.ForeignKey('author.id'), primary_key=True),
    db.Column('book_id', db.ForeignKey('book.id'), primary_key=True)
)

class Author(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(100), index=True, unique=True)
   email = db.Column(db.String(200), index=True, unique=True)
   name = db.Column(db.String(200), index=True, unique=False)
   surname = db.Column(db.String(200), index=True, unique=False)
   password_hash = db.Column(db.String(128))
   books = db.relationship("Book", secondary=association_table, backref="authors", lazy="dynamic")

   def __str__(self):
       return f"<Author {self.username}>"

class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.Text)
   year = db.Column(db.Integer)
   borrowed = db.Column(db.Text)
   #author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

   def __str__(self):
       return f"<Book {self.id} {self.body[:50]} ...>"
