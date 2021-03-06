import unittest
from random import randrange

def is_multiple(n, m):
    if m % n == 0:
        return True
    else:
        return False

def is_even(k):
    while k > 0:
        k -= 2
    return True if k == 0 else False

def minmax(data):
    mn = mx = data[0]
    for i in range(len(data)):
        if data[i] > mx:
            mx = data[i]
        elif data[i] < mn:
            mn = data[i]
    return mn, mx

def sumn(n):
    return sum(range(n))

def sum_sqodd(n):
    sum = 0
    for i in range(n):
        if i%2 != 0:
            sum += i*i
    return sum

def sum_sqodd2(n):
    return sum(i*i for i in range(n) if i%2 != 0)

def choice(data):
    return data[randrange(len(data))]

def odd_product(sequence):
    products = []
    for i in range(len(sequence)):
        for j in range(len(sequence)):
            if i != j:
                if sequence[i] * sequence[j] % 2 != 0:
                    products.append((sequence[i], sequence[j]))
    return products

class TestCh1(unittest.TestCase):

    def test_ismultiple(self):
        self.assertTrue(is_multiple(2, 4))
        self.assertFalse(is_multiple(3, 4))
        self.assertFalse(is_multiple(4, 2))
        with self.assertRaises(ZeroDivisionError):
            is_multiple(0, 10)

    def test_iseven(self):
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(5))

    def test_minmax(self):
        self.assertEqual(minmax([1, 2, 3, 4]), (1, 4))

    def test_sumn(self):
        self.assertEqual(sumn(4), 6)

    def test_sumsqodd(self):
        self.assertEqual(sum_sqodd(6), 35)

    def test_sumsqodd2(self):
        self.assertEqual(sum_sqodd2(6), 35)

    def test_str(self):
        str = "abcdefgh"
        self.assertEqual(str[4], str[4 - len(str)])

    def test_choice(self):
        data = [1, 2, 3, 4, 5, 6, 7]
        self.assertIn(choice(data), data)

if __name__ == '__main__':
    unittest.main()
