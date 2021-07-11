import math
import unittest

class TestStringMethods(unittest.TestCase):
    def isprime(self,n):
        self.assertTrue(n%2 == 0)
        self.assertEqual(n%3,0)
        self.assertFalse(n%5 != 0)
        if n%2 == 0 or n%3 == 0 or n%5 == 0:
            return False
        for i in range(7,math.floor(math.sqrt(n)),2):
            print(math.sqrt(n))
            print(i)
            if n%i == 0:
                return False 
        return True

k = TestStringMethods()
print(k.isprime(54))
