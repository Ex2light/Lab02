from Abstract_Validator import AbstractValidator
import Exceptions

class Validator(AbstractValidator):
    def __init__(self, first, second, type):
        self.first = first
        self.second = second
        self.type = type

    def validate(self):
        if self.type == 'Add':
            if self._Is_Number(self.first) and self._Is_Number(self.second):
                pass
            else:
                raise Exceptions.NotANumber

        elif self.type == 'Divide':
            if self._Is_Number(self.first) and self._Is_Valid_Divider(self.second):
                pass
            elif self._Is_Number(self.first):
                raise Exceptions.NotANumber
            elif self._Is_Number(self.second):
                raise Exceptions.NotANumber
            elif self._Is_Valid_Divider(self.second):
                raise Exceptions.NumberEqualZero
        elif self.type == 'Deriverative':
            if self._Is_String(self.first) and self._Is_Valid_Deriver(self.second):
                pass
            elif self._Is_String(self.first):
                raise Exceptions.NotAString
            elif self._Is_Integer(self.second):
                raise Exceptions.NumberNotAnInteger
            elif self._Is_Not_Lesser_Than_Zero(self.second):
                raise Exceptions.NumberLesserThanZero


    def _Is_Number(self, number):
        if isinstance(number, int):
            return True
        elif isinstance(number, float):
            return True
        else:
            return False

    def _Is_Valid_Divider(self, number):
        if isinstance(number, int) and number != 0:
            return True
        elif isinstance(number, float) and number > 1E-10 and number < -(1E-10):
            return True
        else:
            return False

    def _Is_Valid_Deriver(self, number):
        if isinstance(number, int) and number >= 0:
            return True
        else:
            return False

    def _Is_Integer(self, number):
        if isinstance(number, int):
            return True
        else:
            return False

    def _Is_Not_Lesser_Than_Zero(self, number):
        if number >= 0:
            return True
        else:
            return False

    def _Is_String(self, string):
        if isinstance(string, str):
            return True
        else:
            return False


