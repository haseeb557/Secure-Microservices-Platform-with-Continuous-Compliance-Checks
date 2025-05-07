import unittest
from app import app

class BillingTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_bill_success(self):
        response = self.client.post('/bill', json={
            "customer_id": "123",
            "amount": 100
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("Bill for customer 123 is $100", response.get_data(as_text=True))

    def test_bill_missing_data(self):
        response = self.client.post('/bill', json={
            "amount": 100
        })
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
