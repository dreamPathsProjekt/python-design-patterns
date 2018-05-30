import abc

# Define abstract
class MyAbstractClass(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def abstract_method(self, value):
        pass
        # Required method to implement in subclass

    @abc.abstractproperty
    def abstract_property(self):
        pass
        # Required property


# Implement MyAbstractClass
class MyClass(MyAbstractClass):

    def __init__(self, value=None):
        self._myprop = value

    def abstract_method(self, value):
        self._myprop *= 2 + value

    @property
    def abstract_property(self):
        return self._myprop