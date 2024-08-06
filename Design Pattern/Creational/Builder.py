"""
construct complex objects step by step

initialization code is usually buried inside a monstrous constructor with lots of parameters. 

or scattered all over the client code.
"""

# too much subclasses
# Any new parameter, will require growing this hierarchy

# a giant constructor is bad too

"""
extract the object construction code, and move to separate objects called [builders].

The Builder doesn’t allow other objects to access the product while it’s being built.

** you don’t need to call all of the steps
"""


""" Director ( isn’t strictly necessary)
The director class defines the order in which to execute the building steps,
"""

from abc import ABC, abstractmethod
from typing import Any


class Product1:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass
    @abstractmethod
    def produce_part_a(self) -> None:
        pass
    @abstractmethod
    def produce_part_b(self) -> None:
        pass
    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        """
        should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()
    # take out product
    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")



builder = ConcreteBuilder1()
# Build without a Director class.
print("Custom product: ")
builder.produce_part_a()
builder.produce_part_b()
builder.product.list_parts()


'''
可建構時就決定builder，或者要製造產品時才指定builder

The construction result can be obtained directly from the director only if all products follow the same interface. 
Otherwise, fetch the result from the builder
'''
class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    # 幾套固定的流程
    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


director = Director()
director.builder = builder

print("Standard basic product: ")
director.build_minimal_viable_product()
builder.product.list_parts()

print("\n")

print("Standard full featured product: ")
director.build_full_featured_product()
builder.product.list_parts()

print("\n")

