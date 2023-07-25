import unittest
import base

class TestRand(unittest.TestCase):
    def test_rand(self):
        param1 = 5
        param2 = 5
        result = base.check_guess(param1,param2)
        self.assertTrue(result)

    def test_rand2(self):
        param1 = 5
        param2 = 'a'
        result = base.check_guess(param1,param2)
        self.assertIsInstance(result,TypeError)

    def test_rand3(self):
        param1 = -5
        param2 = -2
        result = base.check_guess(param1,param2)
        self.assertFalse(result)

if(__name__ == '__main__'):
    unittest.main()