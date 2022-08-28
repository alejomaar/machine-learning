import unittest
from .. import Regex

regex =Regex()
class Regex_Test(unittest.TestCase):
    def test_get_integer(self):    
        #Capture the number when it exist 
        self.assertEqual(regex.get_integer('4545'), '4545')
        self.assertEqual(regex.get_integer('4545,78'), '4545')
        self.assertEqual(regex.get_integer('454$^y5fg'), '454')
        self.assertEqual(regex.get_integer('454 between string 789'), '454')
        #return None when number does not exist
        self.assertEqual(regex.get_integer('only string'), None)      

    def test_get_width(self):     
        #Capture the width when it exist
        self.assertEqual(regex.get_width('w100'),'100')
        self.assertEqual(regex.get_width('h100 w200'),'200')
        self.assertEqual(regex.get_width('h100 w200.47'),'200.47')
        self.assertEqual(regex.get_width('h100 w500,47'),'500,47')
        #return None when width does not exist
        self.assertEqual(regex.get_width('h100'),None)
    
    def test_get_height(self):     
        #Capture the height when it exist
        self.assertEqual(regex.get_height('h100'),'100')
        self.assertEqual(regex.get_height('w100 h200'),'200')
        self.assertEqual(regex.get_height('w100 h200.47'),'200.47')
        self.assertEqual(regex.get_height('w100 h500,47'),'500,47')
        #return None when height does not exist
        self.assertEqual(regex.get_height('w100'),None)
    
    def test_get_measure(self):     
        #Capture the height when it exist
        self.assertEqual(regex.get_measure('w100 cm h100cm'),'cm')
        self.assertEqual(regex.get_measure('100 200 mm'),'mm')