"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "67df98a76ds9f78a6s9df78sxx"
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

# GET /: Homepage
@app.route('/')
def home():
    posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    """Show list of posts"""
    return render_template('home.html', posts=posts)

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
    flash(f'{new_user.full_name()} has been created.', 'success')
    return redirect(f'/users/{new_user.id}')

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
    # print('***********')
    # print(f"Pushing update_user for id: {user_id}")
    # print('***********')
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']
    db.session.commit()
    flash(f'{user.full_name()} has been edited', 'success')
    return redirect(f'/users/{user_id}')

# POST /users/[user-id]/delete: Delete the user.
@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    """Delete the user"""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f'{user.full_name()} has been deleted', 'success')
    return redirect('/users')


# GET /users/[user-id]/posts/new : Show form to add a post for that user.
@app.route('/users/<int:user_id>/posts/new')
def new_post(user_id):
    """Show form to add post for that user"""
    user = User.query.get_or_404(user_id)
    return render_template('new-post.html', user=user)

# POST /users/[user-id]/posts/new : Handle add form; add post and redirect to the user detail page.
@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def create_post(user_id):
    user = User.query.get_or_404(user_id)
    title = request.form['title']
    content = request.form['content']
    new_post = Post(title=title, content=content, user=user)
    db.session.add(new_post)
    db.session.commit()
    flash(f'"{new_post.title}" has been created', 'success')
    return redirect(f'/posts/{new_post.id}')

# GET /posts/[post-id] : Show a post. Show buttons to edit and delete the post.
@app.route('/posts/<int:post_id>')
def view_post(post_id):
    """Show the current post based on ID"""
    post = Post.query.get_or_404(post_id)

    return render_template('view-post.html', post=post)

# GET /posts/[post-id]/edit : Show form to edit a post, and to cancel (back to user page).
@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    """Edit th post"""
    post = Post.query.get_or_404(post_id)
    return render_template('edit-post.html', post=post)

# POST /posts/[post-id]/edit : Handle editing of a post. Redirect back to the post view.
@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def update_post(post_id):
    """Update the post"""
    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']
    db.session.commit()
    flash(f'"{post.title}" has been edited.', 'success')
    return redirect(f'/posts/{post_id}')

# POST /posts/[post-id]/delete : Delete the post.
@app.route('/posts/<int:post_id>/delete')
def delete_post(post_id):
    """Delete the post"""
    post = Post.query.get_or_404(post_id)
    print(post)
    temp_id = post.user.id
    print('**** ID', temp_id)
    db.session.delete(post)
    db.session.commit()
    flash(f'"{post.title}" has been deleted', 'success')
    return redirect(f'/users/{temp_id}')