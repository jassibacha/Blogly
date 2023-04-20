"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String(399), 
                        nullable=False,
                        default='http://placekitten.com/400/400')

    def __repr__(self):
        """Show info about pet."""

        u = self
        return f"<Pet {u.id} {u.first_name} {u.last_name} {u.image_url}>"


    def get_full_name(self):
        """Return the full name of the user."""

        return f"{self.first_name} {self.last_name}"