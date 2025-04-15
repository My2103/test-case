import unittest

class MyCalculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Add(self):
        return self.x + self.y

    def Subtract(self):
        return self.x - self.y

    def Multiply(self):
        return self.x * self.y

    def Divide(self):
        if self.y == 0:
            raise ValueError("Cannot divide by zero")
        return self.x / self.y

class TestMyCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up class for MyCalculator tests")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down class after MyCalculator tests")

    def setUp(self):
        # Default initialization, will override in specific tests if needed
        test_name = self.shortDescription()
        print(f"Starting test: {test_name}")

    def tearDown(self):
        test_name = self.shortDescription()
        print(f"End of Test: {test_name}")

# Tests for (3, 2)
    def test_add_3_2(self):
        """Test Addition with (3, 2)"""
        self.calc = MyCalculator(3, 2)
        result = self.calc.Add()
        self.assertEqual(result, 5, "3 + 2 is equal 5")  # 3 + 2 = 5
        self.assertTrue(result > 0, "The result should be positive")  # Result should be positive

    def test_subtract_3_2(self):
        """Test Subtraction with (3, 2)"""
        self.calc = MyCalculator(3, 2)
        result = self.calc.Subtract()
        self.assertEqual(result, 1, "3 - 2 is equal 1")  # 3 - 2 = 1
        self.assertNotEqual(result, 0, "The result should not be 0")  # Result should not be 0

    def test_multiply_3_2(self):
        """Test Multiplication with (3, 2)"""
        self.calc = MyCalculator(3, 2)
        result = self.calc.Multiply()
        self.assertEqual(result, 6, "3 * 2 is equal 6")  # 3 * 2 = 6
        self.assertFalse(result < 0, "The result should not be negative")  # Result should not be negative

    def test_divide_3_2(self):
        """Test Division with (3, 2)"""
        self.calc = MyCalculator(3, 2)
        result = self.calc.Divide()
        self.assertEqual(result, 1.5, "3 / 2 is equal 1.5")  # 3 / 2 = 1.5
        self.assertTrue(result > 0, "The result should be positive")  # Result should be positive

# Tests for (5, 0)
    def test_add_5_0(self):
        """Test Addition with (5, 0)"""
        self.calc = MyCalculator(5, 0)
        result = self.calc.Add()
        self.assertEqual(result, 5, "5 + 0 is equal 5")  # 5 + 0 = 5
        self.assertTrue(result > 0, "The result should be positive")  # Result should be positive

    def test_subtract_5_0(self):
        """Test Subtraction with (5, 0)"""
        self.calc = MyCalculator(5, 0)
        result = self.calc.Subtract()
        self.assertEqual(result, 5, "5 - 0 is equal 5")  # 5 - 0 = 5
        self.assertNotEqual(result, 0, "The result should not be 0")  # Result should not be 0

    def test_multiply_5_0(self):
        """Test Multiplication with (5, 0)"""
        self.calc = MyCalculator(5, 0)
        result = self.calc.Multiply()
        self.assertEqual(result, 0, "5 * 0 is equal 0")  # 5 * 0 = 0
        self.assertFalse(result < 0, "The result should not be positive")  # Result should not be negative

    def test_divide_5_0(self):
        """Test Division by Zero with (5, 0)"""
        self.calc = MyCalculator(5, 0)
        with self.assertRaises(ValueError):
            self.calc.Divide()  # Should raise ValueError

if __name__ == '__main__':
    unittest.main()