import unittest
from names import greet

class TestName(unittest.TestCase):
    def test_women_name(self):
        for i in ["Aga", "Dorota", "Ania"]:
            print('testing', i)
            assert greet(i) == 'hi pretty ' + i

    def test_men_name(self):
        for i in ["Maciek", "Kuba", "Jarek"]:
            print('testing', i)
            assert greet(i) == 'hi ' + i

    def test_women_fullname(self):
        for i in ["Jadwiga Nowak", "Kamila Kowalska", "Joanna Wilk"]:
            print('testing', i)
            assert greet(i) == 'hi pretty ' + i

    def test_men_fullname(self):
        for i in ["Tomasz Nowak", "Dawid Motyka", "Mariusz Kolanko"]:
            print('testing', i)
            assert greet(i) == 'hi ' + i