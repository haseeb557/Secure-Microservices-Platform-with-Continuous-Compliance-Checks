import unittest
from app import app

class TestAuthService(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_login_success(self):
        response = self.client.post('/login', json={'username': 'admin', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login successful!', response.get_data(as_text=True))

    def test_login_failure(self):
        response = self.client.post('/login', json={'username': 'user', 'password': 'wrong'})
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid credentials', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
