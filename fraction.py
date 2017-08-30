__author__ = 'Jianqiu Wang'
__email__ = 'jw2329@cornell.edu'
__date__ = 'Aug 30, 2017'

def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n

# Fraction class
# Implements: addition and equality
# To do: multiplication, division, subtraction and comparison operators(<, >)

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __eq__(self, other):
        """ Overrided original equality
        """
        first_num = self.num * other.den
        second_num = other.num * self.den
        return  first_num == second_num

    def __add__(self, other):
        """ Add two fractions together
        """
        new_num = self.num*other.den + self.den*other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other):
        """ Override substract
        """
        new_num = self.num*other.den - self.den*other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __mul__(self, other):
        """ Override multiplication
        """
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other):
        """ Override division
        """
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

x = Fraction(1,2)
y = Fraction(2,3)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x == y)
