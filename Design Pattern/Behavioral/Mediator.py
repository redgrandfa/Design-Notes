from __future__ import annotations
'''
reduce chaotic dependencies between objects. 

The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object.
'''
'''
    Interface Mediator
        notify(sender)

實現 class ConcreateMediator(Mediator)
組合    componentA 
        #BCD...

        notify(sender){ 
            if (sender == componentA ) 
                reactOnA()
        }
        reactOnA() 
        # BCD...


    class ComponentA  
關聯    m: Mediator
        operationA()  # BCD...

    # class BCD
    
'''



from abc import ABC


class Mediator(ABC):
    """
    declares a method used by components to notify the mediator about various events. 
    may pass the execution to other components.
    """
    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:
    """
    basic: storing a mediator's instance 
    """
    # def __init__(self, mediator: Mediator = None) -> None:
    #     self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


"""Concrete Components 
don't depend on other components.
don't depend on any concrete mediator classes.
"""
class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component 1 does B.")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2 does C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Component 2 does D.")
        self.mediator.notify(self, "D")


# The client code.
c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)

print("Client triggers operation A.")
c1.do_a()

print("")

print("Client triggers operation D.")
c2.do_d()
