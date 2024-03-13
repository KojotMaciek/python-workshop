import unittest
from fizz_buzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        for i in [3, 6, 9, 18]:
            print('testing', i)
            assert fizz_buzz(i) == 'Fizz'

    def test_buzz(self):
        for i in [5, 10, 50]:
            print('testing', i)
            assert fizz_buzz(i) == 'Buzz'

    def test_fizz_buzz(self):
        for i in [15, 30, 75]:
            print('testing', i)
            assert fizz_buzz(i) == 'FizzBuzz'

    def test_number(self):
        for i in [2, 4, 88]:
            print('testing', i)
            assert fizz_buzz(i) == i