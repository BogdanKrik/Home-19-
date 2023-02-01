import pytest

from app.calc import Calculator

class TestCalc:
    def setup (self):
        self.calc = Calculator

    def test_miltiply(self):
         assert self.calc.adding(self, 2, 2 ) ==4

    def test_division(self):
        assert self.calc.division(self, 10, 5) ==2

    def test_subtraction(self):
        assert self.calc.subtraction(self, 20, 7) ==13

    def test_adding(self):
        assert self.calc.adding(self, 3, 3) ==6

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print ('Выполнение теста Teardown')