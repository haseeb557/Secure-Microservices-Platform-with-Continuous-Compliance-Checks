import unittest
from app import app

class ProductTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_existing_product(self):
        response = self.client.get('/product?product_id=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Laptop", response.get_data(as_text=True))

    def test_get_nonexistent_product(self):
        response = self.client.get('/product?product_id=99')
        self.assertEqual(response.status_code, 404)
        self.assertIn("Product not found", response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
