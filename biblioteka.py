from app import app, db
from app.models import Book, Availability, AuthorDetails

@app.shell_context_processor
def make_shell_context():
    return {
        "db" : db,
        "Book" : Book,
        "Availability" : Availability,
        "AuthorDetails" : AuthorDetails
            }