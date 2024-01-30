import unittest
from reversed_strings import reversed_strings
class TestReverseString(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reversed_strings("Hello"), "olleH")
        self.assertEqual(reversed_strings("Python"), "nohtyP")
        self.assertEqual(reversed_strings("12345"), "54321")
        self.assertEqual(reversed_strings("Coding"), "gnidoC")
        self.assertEqual(reversed_strings(""), "")

if __name__ == '__main__':
    unittest.main()
