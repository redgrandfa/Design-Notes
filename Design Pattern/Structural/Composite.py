from __future__ import annotations

"""
compose objects into [tree structures ]
    and then 
    work with these structures as if they were individual objects.

treat both simple and complex elements uniformly.
"""

"""
    client

    #describes operations(common to simple and complex elements)
    interface Component
        execute() 

# complex element
實現 Class Composite 
聚合    children: Component[]  
            #doesn’t know the concrete classes of its children. 

        add(c: Component)
        remove(c: Component)
        getChildren(): Component[]
        execute() { # Delegate to child components }

# simple element
實現 Class Leaf
        execute()

"""

'''
V Open/Closed Principle. 
    introduce new element types into the app 
        without breaking the existing code

X might be difficult to provide a common interface for classes
'''

from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Optionally, 
        declare an interface for setting and accessing 
            a parent of the component in a tree structure. 
        """
        self._parent = parent

    """
    Optionally:
        define the child-management operations in the base  class. 
        downside: these methods will be empty for the leaf-level components.
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        """
        may implement some default behavior
        """
        pass


class Leaf(Component):
    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        delegate the actual work to children 
            and then "sum-up" the result.
            (traverses recursively through all its children)
        """
        results = []
        for child in self._children:
            results.append(child.operation()) 
        return f"Branch({'+'.join(results)})"


def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")



print("Client: simple component:")

simple = Leaf()
client_code(simple)
print("\n")

print("Client: composite tree:")

tree = Composite()

branch1 = Composite()
branch1.add(Leaf())
branch1.add(Leaf())

branch2 = Composite()
branch2.add(Leaf())

tree.add(branch1)
tree.add(branch2)

client_code(tree)
print("\n")
