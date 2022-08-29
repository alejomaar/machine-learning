import unittest
from .. import parallel

class Parallell_Test(unittest.TestCase):
    def test_parallel(self):    
        def plus_one(x):
            return x+1
        lista = [1,2,3,4,5]

        new_list = parallel(plus_one,lista)
        self.assertEqual(new_list, [2,3,4,5,6])
        
if __name__ == '__main__':
    unittest.main()