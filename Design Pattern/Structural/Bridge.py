from __future__ import annotations
from abc import ABC, abstractmethod


'''
split a large class into two separate 
    hierarchies—
        abstraction and
        implementation—
    which can be developed independently 

    # orthogonal (independent) dimensions
'''

# switching from inheritance to the object composition

# https://refactoring.guru/images/patterns/diagrams/bridge/structure-en-indexed.png

'''
client:
    abstraction.filed1...

#high-level control logic
        Abstraction  
            i:Implementation
    繼承 Refined Abstractions

# do the actual low-level work.
    聚合 Implementation 
    實現 Concrete Implementations
'''

# client -> Abstraction -> Implementation
# 人          遙控器          裝置
#              電視遙控器       電視
#              冷氣遙控器       冷氣



class Abstraction:
    """
    defines the interface for the "control" part of the two class hierarchies. 
    """
    def __init__(self, implementation: Implementation) -> None:
        # a reference to the Implementation object
        self.implementation = implementation

    # delegates all of the real work to this object.
    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")



class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass


"""
Each Concrete Implementation corresponds to a specific platform
using that platform's API.
"""
class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: the result on the platform B."


def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation(), end="")



implementation = ConcreteImplementationA()
abstraction = Abstraction(implementation)
client_code(abstraction) 
#client code should only depend on the Abstraction class

print("\n")

implementation = ConcreteImplementationB()
abstraction = ExtendedAbstraction(implementation)
client_code(abstraction)

