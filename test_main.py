import unittest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app instance

client = TestClient(app) # Create a test client to interact with your app

class TestCalculatorAPI(unittest.TestCase):

    def test_read_root(self):
        """Test the root endpoint '/'."""
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to the Scientific Calculator API. Access operations via /sqrt, /factorial, /ln, /power endpoints. For UI, go to /ui"})

    # --- Square Root Tests ---
    def test_square_root_valid(self):
        """Test square root with a valid positive number."""
        response = client.get("/sqrt/25")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 5.0})

    def test_square_root_valid_decimal(self):
        """Test square root with a valid decimal number."""
        response = client.get("/sqrt/2.25")
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()["result"], 1.5, places=5) # Use assertAlmostEqual for floats

    def test_square_root_invalid_negative(self):
        """Test square root with an invalid negative number."""
        response = client.get("/sqrt/-4")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"detail": "Cannot calculate square root of a negative number"})

    # --- Factorial Tests ---
    def test_factorial_valid_positive_integer(self):
        """Test factorial with a valid positive integer."""
        response = client.get("/factorial/5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 120})

    def test_factorial_valid_zero(self):
        """Test factorial with zero."""
        response = client.get("/factorial/0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 1})

    def test_factorial_invalid_negative(self):
        """Test factorial with an invalid negative number."""
        response = client.get("/factorial/-3")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"detail": "Factorial is not defined for negative numbers"})

    def test_factorial_invalid_large(self):
        """Test factorial with a very large number (expecting potential ValueError handling)."""
        response = client.get("/factorial/200") # Test with a large number that might cause issues
        self.assertEqual(response.status_code, 400) # Expecting 400 because of potential out-of-range


    # --- Natural Logarithm Tests ---
    def test_ln_valid_positive(self):
        """Test natural logarithm with a valid positive number."""
        response = client.get("/ln/2.71828") # Close to e
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()["result"], 1.0, places=4)

    def test_ln_invalid_zero(self):
        """Test natural logarithm with zero (invalid)."""
        response = client.get("/ln/0")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"detail": "Natural logarithm is not defined for non-positive numbers"})

    def test_ln_invalid_negative(self):
        """Test natural logarithm with a negative number (invalid)."""
        response = client.get("/ln/-1")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"detail": "Natural logarithm is not defined for non-positive numbers"})

    # --- Power Function Tests ---
    def test_power_valid_positive_base_exponent(self):
        """Test power function with valid positive base and exponent."""
        response = client.get("/power/2/3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 8.0})

    def test_power_valid_decimal_base_exponent(self):
        """Test power function with decimal base and exponent."""
        response = client.get("/power/1.5/2.5")
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()["result"], 2.75567596, places=5)

    def test_power_valid_negative_exponent(self):
        """Test power function with a negative exponent."""
        response = client.get("/power/2/-2")
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()["result"], 0.25, places=5)

    def test_power_valid_zero_base(self):
        """Test power function with zero base."""
        response = client.get("/power/0/5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 0.0})

    def test_power_valid_base_to_zero_power(self):
        """Test power function with exponent zero."""
        response = client.get("/power/5/0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 1.0})


if __name__ == '__main__':
    unittest.main()