# -*- coding: Latin-1 -*-

import unittest

def plus(a, b):
    return a+b

class TestAddition(unittest.TestCase):
    def test_addition(self):
        result = plus(36,6)
        self.assertEqual(result, 42)
        
if __name__ == '__main__':
    unittest.main()