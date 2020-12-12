from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

# Create your tests here.
class loginTest(TestCase):
    def test_login_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_halaman_login(self):
        response = Client().get('/')
        html_response = response.content.decode('utf8')
        self.assertIn("Please LogIn Here!", html_response)
        self.assertIn("Username", html_response)
        self.assertIn("Password", html_response)
        self.assertIn("Don't have an account? Create one <a class=\"to-register-ref\" href=\"register/\">here</a>", html_response)
        self.assertIn("Log In", html_response)

    def test_halaman_registrasi(self):
        response = Client().get('/register/')
        html_response = response.content.decode('utf8')
        self.assertIn("Please Register Here!", html_response)
        self.assertIn("First Name", html_response)
        self.assertIn("Last Name", html_response)
        self.assertIn("Username", html_response)
        self.assertIn("Password", html_response)
        self.assertIn("Password Confirmation", html_response)
        self.assertIn("Register", html_response)

    def test_simpan_user(self):
        Client().post('/register/', {'first_name': 'James', 'last_name': 'Frederix', 'username':'jmshaha', 'password1':'boba3223', 'password2':'boba3223'})
        self.assertEquals(User.objects.all().count(), 1)

    def test_halaman_setelah_login(self):
        Client().post('/register/', {'first_name': 'James', 'last_name': 'Frederix', 'username':'jmshaha', 'password1':'boba3223', 'password2':'boba3223'})
        response = Client().post('/', {'username':'jmshaha', 'password':'boba3223'})
        html_response = response.content.decode('utf8')
        self.assertIn("Good", html_response)
        self.assertIn("James Frederix", html_response)
        self.assertIn("Log Out", html_response)

    def test_halaman_gagal_login(self):
        response = Client().post('/', {'username':'jmshaha', 'password':'boba3223'})
        html_response = response.content.decode('utf8')
        self.assertIn("Please LogIn Here!", html_response)
        self.assertIn("Username", html_response)
        self.assertIn("Password", html_response)
        self.assertIn("Don't have an account? Create one <a class=\"to-register-ref\" href=\"register/\">here</a>", html_response)
        self.assertIn("Log In", html_response)
        self.assertIn("username or password is not correct", html_response)