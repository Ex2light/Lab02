import abc


class AbstractValidator(object, _metaclass_=abc.ABCMeta):
    @abc.abstractmethod
    def validate(self):
        """Validate the input"""
