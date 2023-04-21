"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """Users Model"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String(399), 
                        nullable=False,
                        default='http://placekitten.com/400/400')

    posts = db.relationship('Post', backref="user", cascade="all, delete")

    def __repr__(self):
        """Show info about user."""
        u = self
        return f"<User {u.id} {u.first_name} {u.last_name} {u.image_url}>"


    def full_name(self):
        """Return the full name of the user."""

        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    """Post Model"""
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        """Show info about post."""
        p = self
        return f"<Post id={p.id} user_id={p.user_id} title={p.title}>"

    def friendly_date(self):
        """Return the created_at date in an actually readable format"""
        return self.created_at.strftime('%B %d, %Y')
