from __future__ import annotations
'''
separate algorithms from the objects on which they operate.
'''
'''
place the new behavior into a separate class called visitor

uses a technique called Double Dispatch
delegate this choice to objects we’re passing to the visitor as an argument? Since the objects know their own classes, they’ll be able to pick a proper method on the visitor


if we extract a common interface for all visitors, all existing nodes can work with any visitor you introduce into the app. 
If you find yourself introducing a new behavior related to nodes, all you have to do is implement a new visitor class.
'''
'''
client code { 
# clients aren’t aware of all the concrete element classes (work by Interface)
    element(new ConcreteVisitor())
}


    Interface Element
        accept(v: Visitor)

        
    # redirect the call to the proper visitor’s method (by overloading)
實現 Class ConcreteElementA
        featureA()
實現     accept(v: Visitor){
            v.visit(this)   # Double Dispatch?
        }
    Class ConcreteElementB
        featureA()
        accept(v ...


    Interface Visitor
多載     visit(e:ElementA)
多載     visit(e:ElementB)

實現 Class ConcreteVisitors  #可以拆多個class
實現     visit(e:ElementA){
            e.featureA()    # Double Dispatch?
        }
        visit(e:ElementB){ ...}

node接待visitor，把自己傳給visitor 'visit' 讓visitor控制node執行
'''


from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class ConcreteComponentA(Component):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_component_a(self)

    def featureA(self) -> str:
        """
        Concrete Components may have methods that don't exist in their
        base class or interface. 
        The Visitor is still able to use these methods 
            since it's aware of the component's concrete class.
        """
        return "A"


class ConcreteComponentB(Component):
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_component_b(self)

    def featureB(self) -> str:
        return "B"


class Visitor(ABC):
    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass



class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.featureA()} + ConcreteVisitor1")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.featureB()} + ConcreteVisitor1")


class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.featureA()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.featureB()} + ConcreteVisitor2")


def client_code(components: List[Component], visitor: Visitor) -> None:
    """
    The client code can run visitor operations over any set of elements without figuring out their concrete classes. 
    The accept operation directs a call to
    the appropriate operation in the visitor object.
    """

    for component in components:
        component.accept(visitor)


components = [ConcreteComponentA(), ConcreteComponentB()]

visitor1 = ConcreteVisitor1()
client_code(components, visitor1)

visitor2 = ConcreteVisitor2()
client_code(components, visitor2)
