from datetime import datetime
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), index=True, unique=True)
    author = db.Column(db.String(200), index=True, unique=True)
    genre = db.Column(db.String(150), index=True, unique=True)
    year_publication = db.Column(db.Integer, index=True)
    availability_status = db.relationship("Availability", backref="shelf", lazy="dynamic")
    author_details = db.relationship("AuthorDetails", backref="author_name", lazy="dynamic")

    def __str__(self):
        return f"<Book {self.title}>"


class Availability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    on_shelf = db.Column(db.Boolean)
    borrower = db.Column(db.String(200), index=True, unique=True, default="None")
    date_borrowed = db.Column(db.DateTime, index=True, default=None)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f"<Availability {self.book_id} {self.on_shelf} {self.borrower}>"

class AuthorDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(200), db.ForeignKey('book.author'))
    year_of_birth = db.Column(db.Integer)
    nationality = db.Column(db.String(50))

    def __str__(self):
        return f"<AuthorDetails {self.author} {self.title}>"