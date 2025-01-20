import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_multiply(self):
        assert self.calc.multiply(3, 4) == 12

    def test_division(self):
        assert self.calc.division(8, 2) == 4

    def test_subtraction(self):
        assert self.calc.subtraction(5, 3) == 2

    def test_adding(self):
        assert self.calc.adding(7, 2) == 9