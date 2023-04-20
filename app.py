"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "67df98a76ds9f78a6s9df78sxx"
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

# GET /: Redirect to list of users. (We’ll fix this in a later step).
@app.route('/')
def home():
    """Show list of all users"""
    return redirect('/users')

# GET /users: Show all users. Make these links to view the detail page for the user. Have a link here to the add-user form.
@app.route('/users')
def users_list():
    """Show list of all users"""
    users = User.query.all()
    return render_template('list.html', users=users)

# GET /users/new: Show an add form for users
@app.route('/users/new')
def users_new():
    """Form to add new user"""
    return render_template('new-user.html')

# POST /users/new: Process the add form, adding a new user and going back to /users
@app.route('/users/new', methods=["POST"])
def users_create():
    """Form to add new user"""
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()
    flash(f'{new_user.get_full_name()} has been created.', 'success')
    return redirect('/')

# GET /users/[user-id]: Show information about the given user. Have a button to get to their edit page, and to delete the user.
@app.route('/users/<int:user_id>')
def view_user(user_id):
    """Show the current user based on ID"""
    user = User.query.get_or_404(user_id)
    return render_template('view-user.html', user=user)

# GET /users/[user-id]/edit: Show the edit page for a user. Have a cancel button that returns to the detail page for a user, and a save button that updates the user.
@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """Edit the users info"""
    user = User.query.get_or_404(user_id)
    print('***********')
    print(f"Accessing edit page of {user_id}")
    print('***********')
    return render_template('edit-user.html', user=user)

# POST /users/[user-id]/edit: Process the edit form, returning the user to the /users page.
@app.route('/users/<int:user_id>/edit', methods=["POST"])
def update_user(user_id):
    """Update the user's info"""
    user = User.query.get_or_404(user_id)
    print('***********')
    print(f"Pushing update_user for id: {user_id}")
    print('***********')
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']
    db.session.commit()
    flash(f'{user.get_full_name()} has been edited', 'success')
    return redirect(f'/users/{user_id}')

# POST /users/[user-id]/delete: Delete the user.
@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    """Delete the user"""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f'{user.get_full_name()} has been deleted', 'success')
    return redirect('/users')
