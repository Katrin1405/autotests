import pytest
from app.Calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_correct(self):
        assert self.calc.multiply(self, 3, 8) == 24

    def test_division_correct(self):
        assert self.calc.division(self, 144, 12) == 12

    def test_subtraction_correct(self):
        assert self.calc.subtraction(self, 15, 3) == 12

    def test_adding_correct(self):
        assert self.calc.adding(self, 20, 10) == 30
