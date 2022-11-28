import unittest

from SpecProj import fill_array, three_or_less


class TestMethods(unittest.TestCase):
    def test_three_or_less_1(self):
        test_array = three_or_less(["hello", "2", "world", ":-)"])
        self.assertEqual(test_array, ["2", ":-)"])


    def test_three_or_less_2(self):
        test_array = three_or_less(["1234", "1567", "-2", "computer science"])
        self.assertEqual(test_array, ["-2"])


    def test_three_or_less_3(self):
        test_array = three_or_less(["Russia", "Denmark", "Kazan"])
        self.assertEqual(test_array, [ ])
     

if __name__ == '__main__':
    unittest.main()
