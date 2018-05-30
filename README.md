# Python Design Patterns

Design Pattern Implementations in Python 3

## Categories

### Creational

Object Creation

### Structural

Object Relationships

### Behavioural

Object Interaction & Responsibility

## Python Interfaces

[Abstract & Implementation classes](./interfaces/abstract_implementation.py)

- Originally Python had intermediate classes used as `mixins`. This is though an __implementation__ not an __abstraction.__
- Best practice: to code towards abstraction vs implementation.
- Solution: `Abstract Base Class` ,appeared in `Python 2.6`& `Python 3.0`, introduced by `PEP3119`

ABC inherits from object and uses abc module

`Python 2.*`

```Python
import abc

class MyAbstractClass():
    # Define abstract
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def abstract_method(self, value):
        # Required method to implement in subclass

    @abc.abstractproperty
    def abstract_property(self):
        # Required property
```

`Python 3.*`

```Python
import abc

# Define abstract
class MyAbstractClass(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def abstract_method(self, value):
        # Required method to implement in subclass

    @abc.abstractproperty
    def abstract_property(self):
        # Required property
```

## Strategy Pattern

- Family of Algorithms
- Encapsulate them
- Make them interchangeable
- Algorithms vary independently