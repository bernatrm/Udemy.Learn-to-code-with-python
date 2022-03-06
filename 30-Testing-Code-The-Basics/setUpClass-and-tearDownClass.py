import unittest

class TestOperations(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls): # Tipically used when we have any cost operation, 
                         # and don't want to execute it before  / after every testTypically used when we have any high cost operation, and don't want to execute it before / after every test
        print("This will run ONCE before the test suite starts")
    
    def setUp(self):
        print("This will run before EACH test")

    def tearDown(self) -> None:
        print("This will run after EACH test")

    @classmethod
    def tearDownClass(cls):
        print("This will run ONCE after the test finishes")
    
    def test_stuff(self):
        self.assertEqual(1, 1)

    def test_more_stuff(self):
        self.assertEqual([], [])

if __name__ == "__main__":
    unittest.main()