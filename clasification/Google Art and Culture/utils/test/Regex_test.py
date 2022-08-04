import unittest
from utils.Regex import Regex

regex =Regex()
class Regex_Test(unittest.TestCase):
    def test_get_digit(self):     
        self.assertEqual(regex.get_digit('4545'), '4545')
        self.assertEqual(regex.get_digit('454$^y5fg'), '454')
        self.assertEqual(regex.get_digit('454 between string 789'), '454')

    def test_get_digit_failure(self):
        regex =Regex()
        self.assertEqual(regex.get_digit('only string'), None)
