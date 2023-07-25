import unittest
import base

class TestBase(unittest.TestCase):
    def setUp(self):
        print('test initial')
    def test_sum_func(self):
        param1 = 4
        param2 = 2
        result = base.sum_func(param1,param2)
        self.assertEqual(result,2)

    def test_sum_func2(self):
        param1 = 12
        param2 = 'nelson'
        result = base.sum_func(param1,param2)
        self.assertTrue(isinstance(result,TypeError))

    def test_sum_func3(self):
        param1 = 1
        param2 =0
        result = base.sum_func(param1,param2)
        self.assertTrue(isinstance(result,ZeroDivisionError))
    
    def tearDown(self):
        print('cleaning test')

   
if(__name__ == '__main__'):
    unittest.main()