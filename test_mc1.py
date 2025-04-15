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
            raise ValueError("Division by zero is not allowed")
        return self.x / self.y

class TestMyCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up class for MyCalculator tests")
    
    @classmethod
    def tearDownClass(cls):
        print("Tearing down class after MyCalculator tests")
    
    def setUp(self):
        # Will initialize specific values in each test method
        print(f"Test: {self.shortDescription()}")
    
    def tearDown(self):
        print(f"End of Test: {self.shortDescription()}")
    
    def test_case_3_2_add(self):
        """Test Add with inputs (3, 2)"""
        self.calc = MyCalculator(3, 2)
        result = self.calc.Add()
        self.assertEqual(result, 5, "3 + 2 should equal 5")
        self.assertTrue(result > 0, "Addition result should be positive")
    
    def test_case_3_2_subtract(self):
        """Test Subtract with inputs (3, 2)"""
        self.calc = MyCalculator(3, 2)
        result = self.calc.Subtract()
        self.assertEqual(result, 1, "3 - 2 should equal 1")
        self.assertNotEqual(result, 0, "Subtraction result should not be 0")
    
    def test_case_3_2_multiply(self):
        """Test Multiply with inputs (3, 2)"""
        self.calc = MyCalculator(3, 2)
        result = self.calc.Multiply()
        self.assertEqual(result, 6, "3 * 2 should equal 6")
        self.assertFalse(result == 0, "Multiplication result should not be 0")
    
    def test_case_3_2_divide(self):
        """Test Divide with inputs (3, 2)"""
        self.calc = MyCalculator(3, 2)
        result = self.calc.Divide()
        self.assertEqual(result, 1.5, "3 / 2 should equal 1.5")
        self.assertTrue(result > 0, "Division result should be positive")
    
    def test_case_5_0_add(self):
        """Test Add with inputs (5, 0)"""
        self.calc = MyCalculator(5, 0)
        result = self.calc.Add()
        self.assertEqual(result, 5, "5 + 0 should equal 5")
        self.assertTrue(result > 0, "Addition result should be positive")
    
    def test_case_5_0_subtract(self):
        """Test Subtract with inputs (5, 0)"""
        self.calc = MyCalculator(5, 0)
        result = self.calc.Subtract()
        self.assertEqual(result, 5, "5 - 0 should equal 5")
        self.assertNotEqual(result, 0, "Subtraction result should not be 0")
    
    def test_case_5_0_multiply(self):
        """Test Multiply with inputs (5, 0)"""
        self.calc = MyCalculator(5, 0)
        result = self.calc.Multiply()
        self.assertEqual(result, 0, "5 * 0 should equal 0")
        self.assertFalse(result > 0, "Multiplication result should not be positive")
    
    def test_case_5_0_divide(self):
        """Test Divide with inputs (5, 0)"""
        self.calc = MyCalculator(5, 0)
        with self.assertRaises(ValueError):
            self.calc.Divide()

if __name__ == '__main__':
    unittest.main()