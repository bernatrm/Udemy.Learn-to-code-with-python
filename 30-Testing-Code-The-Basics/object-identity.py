import unittest

class IdentityTests(unittest.TestCase):
    def test_identicality(self):
        a = [1, 2, 3]    
        b = a
        c = [1, 2, 3]

        self.assertEqual(a, b) #Is same value
        self.assertEqual(a, c)

        self.assertIs(a, b) #Is same object
        self.assertIsNot(b, c)

if __name__ == "__main__":
    unittest.main()