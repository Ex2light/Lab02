from Calculator import Calculator
from unittest import TestCase
import Exceptions

class TestCalculator(Calculator):
    def test_correct_adding_int_int(self):
        c = Calculator()
        first = 20
        second = 25
        expected_resault = 45
        self.assertEqual(expected_resault, c.Add(first, second))

    def test_correct_adding_float_int(self):
        c = Calculator()
        first = 10
        second = 0.5
        expected_resault = 10.5
        self.assertAlmostEqual(expected_resault, c.Add(first, second))

    def test_correct_adding_float_float(self):
        c = Calculator()
        first = 0.3
        second = 3.4
        expected_resault = 3.7
        self.assertAlmostEqual(expected_resault, c.Add(first, second))

    def test_adding_string_raising_exception(self):
        c = Calculator()
        first = 'grota'
        second = 3.4
        self.assertRaises(Exceptions.NotANumber, c.Add,(first, second))
###################################################################################################################

    def test_correct_divide_int_int(self):
        c = Calculator()
        first = 5
        second = 2
        expected_resault = 2.5
        self.assertAlmostEqual(expected_resault, c.Divide(first, second))

    def test_correct_divide_float_int(self):
        c = Calculator()
        first = 7.8
        second = 2
        expected_resault = 3.9
        self.assertAlmostEqual(expected_resault, c.Divide(first, second))

    def test_correct_divide_float_float(self):
        c = Calculator()
        first = 5.5
        second = 2.2
        expected_resault = 2.5
        self.assertAlmostEqual(expected_resault, c.Divide(first, second))

    def test_correct_divide_float_zero(self):
        c = Calculator()
        first = 5.9
        second = 0
        self.assertAlmostEqual(c.Divide(first, second))

    def test_correct_divide_int_zero(self):
        c = Calculator()
        first = 5
        second = 0
        self.assertAlmostEqual(c.Divide(first, second))

