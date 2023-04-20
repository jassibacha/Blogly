from unittest import TestCase

from app import app
from models import db, User

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
            resp = client.get('/users/1/edit')
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
            resp = client.post('/users/1/edit', data=form_data, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Jane Smith</h1>', html)
            self.assertIn('https://example.com/new_image.jpg', html)
            

    def test_users_create(self):
        """Test creating a suer"""
        with app.test_client() as client:
            d = {"first_name": "Jane", "last_name": "Doe", "image_url": "https://example.com/image2.jpg"}
            resp = client.post('/users/new', data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Users</h1>', html)
            self.assertIn('Jane Doe', html)
            