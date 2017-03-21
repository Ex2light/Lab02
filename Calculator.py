from Validator import Validator
from Abstract_Calculator import AbstractCalculator
from sympy import diff

class Calculator(AbstractCalculator):
    def Add(self, first_argument, second_argument, type):
        addValidate = Validator(first_argument, second_argument)
        addValidate.validate(first_argument, second_argument, 'Add')
        return first_argument + second_argument

    def Divide(self, first_argument, second_argument, type):
        divideValdiate = Validator(first_argument, second_argument)
        divideValdiate.validate(first_argument, second_argument, 'Divide')
        return  first_argument/second_argument

    def Derivative(self, first_argument, second_argument, type):
        derivativeValidate = Validator(first_argument, second_argument, 'Deriverative')
        derivativeValidate.validate()
        return diff(first_argument, 'x', second_argument)

