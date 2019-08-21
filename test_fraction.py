from fraction import Fraction
import pytest


def test_fraction_addition():
    a = Fraction(1,2)
    b = Fraction(1,4)
    c = a.Addition(b)
    assert c.num == 3
    assert c.denom == 4

def test_fraction_subtraction():
    a = Fraction(1,2)
    b = Fraction(1,4)
    c = a.Subtraction(b)
    assert c.num == 1
    assert c.denom == 4

def test_fraction_multiplication():
    a = Fraction(1,2)
    b = Fraction(1,4)
    c = a.Multiplication(b)
    assert c.num == 1
    assert c.denom == 8

def test_fraction_division():
    a = Fraction(1,2)
    b = Fraction(1,4)
    c = a.Division(b)
    assert c.num == 2
    assert c.denom == 1

def test_fraction_inverse():
    a = Fraction(1, 2)
    b = a.Inverse()

    assert b.num == 2
    assert b.denom == 1

def test_fraction_float():
    a = Fraction(1,2)
    assert float(a) == 0.5

def test_fraction_exceptions():
    with pytest.raises(Exception):
        assert Fraction(1.5, 3)
        assert Fraction(3, 4.5)

