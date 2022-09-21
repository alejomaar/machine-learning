import unittest
from .. import Regex

regex =Regex()
class Regex_Test(unittest.TestCase):
    def test_get_date(self):    
        #Capture the number when it exist 
        self.assertEqual(regex.get_date('2021,  2020'), 2021)
        self.assertEqual(regex.get_date('2021-01-09'), 2021)
        self.assertEqual(regex.get_date('late 20th century'), 1900)
        self.assertEqual(regex.get_date('18th century'), 1700)
        self.assertEqual(regex.get_date('Second half of the 1750s'), 1750)
        self.assertEqual(regex.get_date('2nd half of the 19th c.'), 1800)
        
        
        #return None when number does not exist
        self.assertEqual(regex.get_date(float("nan")),None)
        self.assertEqual(regex.get_date('only string'), None)      

    def test_get_width(self):     
        #Capture the width when it exist
        self.assertEqual(regex.get_width('w100'),'100')
        self.assertEqual(regex.get_width('h100 w200'),'200')
        self.assertEqual(regex.get_width('h100 w200.47'),'200.47')
        self.assertEqual(regex.get_width('h100 w500,47'),'500,47')
        #return None when width does not exist
        self.assertEqual(regex.get_width('text'),None)
    
    def test_get_height(self):     
        #Capture the height when it exist
        self.assertEqual(regex.get_height('h100'),'100')
        self.assertEqual(regex.get_height('w100 h200'),'200')
        self.assertEqual(regex.get_height('w100 h200.47'),'200.47')
        self.assertEqual(regex.get_height('w100 h500,47'),'500,47')
        #return None when height does not exist
        self.assertEqual(regex.get_height('text'),None)
    
    def test_get_measure(self):     
        #Capture the height when it exist
        self.assertEqual(regex.get_measure('w100 cm h100cm'),'cm')
        self.assertEqual(regex.get_measure('100 200 mm'),'mm')