import unittest
class TestArithmetic (unittest.TestCase):

    def test_square(self):
        num = 5
        result =num**2
        self.assertEqual(result, 25)
if __name__ == '__main__':
    unittest.main()
