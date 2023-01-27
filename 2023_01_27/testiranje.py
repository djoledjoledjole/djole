class Calculator: #klasa je gomila metoda
    def saberi(self, a, b):
        return a+b
    def oduzmi(self, a, b):
        return a-b
calc = Calculator()

broj1 = 2
broj2 = 3
ocekivano = broj1 + broj2

dobijeno = calc.saberi(broj1,broj2)

print(ocekivano == dobijeno)
#-----------------------------------------------------
import unittest

class TestKalkulator(unittest.TestCase):
    def test_sabiranje(self):
        kalkulator = Calculator()
        ocekivano = 5
        dobijeno = kalkulator.saberi(2,3)

        self.assertEqual(ocekivano, dobijeno)

unittest.main()