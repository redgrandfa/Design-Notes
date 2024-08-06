from __future__ import annotations

'''
define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.
'''
'''
The original class, called context, must have a field for storing a reference to one of the strategies. 
delegates the work to a strategy object instead of executing it on its own.

the context doesn’t know much about strategies. (through generic interface)
the client passes the desired strategy to the context. 

strategies only exposes a single method for triggering the algorithm.
'''

''' Applicability
when you want to use variants of an algorithm within an object and be able to switch algorithm during runtime.

when you have a lot of similar classes that only differ in the way they execute some behavior

isolate some business logic, not need to be in context

when your class has a massive conditional statement that switches between different variants of the same algorithm.
'''



'''
client{
    str = new ConcreteStrategy()
    context.setStrategy(str)
    context.doSth()         

    ...
}

    Class Context    #defines the interface of interest to clients.
聚合     strategy: Strategy
        setStrategy(strategy)
        doSth(){       #delagete to a strategy object
            strategy.execute()
        }

    Interface Strategy # 可被 Lambda function取代
        execute(data)

實現 Class ConcreteStrategies
實現     execute(data)
'''



from abc import ABC, abstractmethod
from typing import List


class Context():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        does not know the concrete class of a strategy. 
        via the Strategy interface.
        """
        return self._strategy

    # provides a setter to change strategy at runtime.
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        The Context delegates some work to the Strategy object 
        (seperate algorithms)
        """
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List):
        pass


"""
The interface makes Concrete Strategies interchangeable in the Context.
"""
class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


context = Context(ConcreteStrategyA())
print("Client: Strategy = normal sorting.")
context.do_some_business_logic()
print()

print("Client: Strategy = reverse sorting.")
context.strategy = ConcreteStrategyB()
context.do_some_business_logic()
