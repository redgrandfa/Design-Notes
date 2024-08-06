'''
defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.
'''
'''Problem
If all processing classes had a common interface or a base class, you’d be able to eliminate the conditionals in client code and use polymorphism.
'''
'''SOL
The Template Method pattern suggests that you break down an algorithm into methods, and put a series of calls to these methods inside a single template method.
'''
'''Applicability
extend only particular steps of an algorithm, but not the whole algorithm or its structure.

when you have several classes that contain almost identical algorithms with some minor differences.
'''
'''
    class AbstractClass
        templateMethod(){ #不被子類覆寫
            step1()
            step2()
        }
        step1()
        step2()

繼承 class ConreateClass1 
覆寫     step1()
        ...
繼承 class ConreateClass2 
覆寫     step1()
        ...
'''
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self) -> None:
        """
        The template method defines the skeleton of an algorithm.
        """

        self.step1()
        self.step2()

    def step1(self) -> None:
        print("AbstractClass says: step1")

    def step2(self) -> None:
        print("AbstractClass says: step2")


class ConcreteClass1(AbstractClass):
    def step1(self) -> None:
        print("ConcreteClass1 says: Implemented step1")

class ConcreteClass2(AbstractClass):
    def step2(self) -> None:
        print("ConcreteClass2 says: Implemented step2")

def client_code(abstract_class: AbstractClass) -> None:
    """
    Client code does not have to know the concrete class of an object it works with, 
    """
    abstract_class.template_method()


print("Same client code can work with different subclasses:")
client_code(ConcreteClass1())
print("")

print("Same client code can work with different subclasses:")
client_code(ConcreteClass2())
