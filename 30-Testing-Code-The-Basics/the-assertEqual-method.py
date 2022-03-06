import unittest

class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
        self.assertEqual("d+e+f".split("+"), ["d", "e", "g"])

    def test_count(self):
        self.assertEqual("beautiful".count("z"), 2)

if __name__ == "__main__":
    unittest.main()