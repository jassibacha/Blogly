from unittest import TestCase

from app import app
from models import db, User, Post

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()


class UserViewsTestCase(TestCase):
    """Tests for views for users."""

    def setUp(self):
        """Add sample user."""

        User.query.delete()

        user = User(first_name="John", last_name="Doe", image_url="https://example.com/image.jpg")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()

    def test_user_list(self):
        """Test the main user list"""
        with app.test_client() as client:
            resp = client.get('/users')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('John Doe', html)


    def test_show_user(self):
        """Test displaying a single user page"""
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>John Doe</h1>', html)
            self.assertIn('https://example.com/image.jpg', html)
            

    def test_edit_user(self):
        """Test that user is edited correctly"""
        with app.test_client() as client:
            # Send GET request to edit user page
            resp = client.get(f'/users/{self.user_id}/edit')
            html = resp.get_data(as_text=True)

            # Verify that the response contains the correct user information
            self.assertIn('value="John"', html)
            self.assertIn('value="Doe"', html)
            self.assertIn('value="https://example.com/image.jpg"', html)
            
            # Send POST request to edit user page with updated information
            form_data = {
                'first_name': 'Jane',
                'last_name': 'Smith',
                'image_url': 'https://example.com/new_image.jpg'
            }
            resp = client.post(f'/users/{self.user_id}/edit', data=form_data, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Jane Smith</h1>', html)
            self.assertIn('https://example.com/new_image.jpg', html)
            

    def test_users_create(self):
        """Test creating a user"""
        with app.test_client() as client:
            d = {"first_name": "Jane", "last_name": "Doe", "image_url": "https://example.com/image2.jpg"}
            resp = client.post('/users/new', data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Jane Doe', html)


class PostViewsTestCase(TestCase):
    """Tests for views for posts."""

    def setUp(self):
        """Add sample post."""

        Post.query.delete()
        User.query.delete()

        user = User(first_name="John", last_name="Doe", image_url="https://example.com/image.jpg")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

        #Post.query.delete()

        # NOTE: We cannot hard code the user id, it needs to be dynamic. Manually putting 1 broke this.
        post = Post(title="My first post", content="This is my first post content.", created_at="2023-04-17 09:15:32", user_id=self.user_id)
        db.session.add(post)
        db.session.commit()

        self.post_id = post.id

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()
        Post.query.delete()
        User.query.delete()
        db.session.commit()
        #User.query.delete() #Here, we create a Post object associated with the User object we created earlier, and then delete the Post object before deleting the User object in the tearDown method.
        #db.session.commit()

    def test_home(self):
        """Test the main post list"""
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('My first post', html)


    def test_show_post(self):
        """Test displaying a single post page"""
        with app.test_client() as client:
            resp = client.get(f"/posts/{self.post_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>My first post</h1>', html)
            self.assertIn('This is my first post content.', html)
