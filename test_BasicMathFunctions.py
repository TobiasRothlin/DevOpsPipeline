from BasicMathFunctions import add,multiply,sin
import unittest

class TestBasicMathFunctions(unittest.TestCase):
    def test_Add(self):
        self.assertEqual(add(2,3), 5)

    def test_Multiply(self):
        self.assertEqual(multiply(2,3), 6)
    
    def test_Sin(self):
        self.assertEqual(sin(0), 0)
   

if __name__ == '__main__':
    unittest.main()