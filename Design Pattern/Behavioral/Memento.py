from __future__ import annotations
'''
save and restore the previous state of an object 
    without revealing the details of its implementation.
'''
'''Problem:
To allow other objects to write and read data to and from a snapshot, you’d probably need to make its fields public. 
That would expose all the editor’s states,
'''

'''
The Memento pattern delegates creating the state snapshots to the actual owner of that state. 

storing the copy of the object’s state in a special object called memento. 
The contents of the memento aren’t accessible to any other object except the one that produced it. 

Other objects must communicate with mementos using a limited interface which may allow fetching the snapshot’s metadata (creation time, the name of the performed operation, etc.), 
    but not the original object’s state contained in the snapshot.
'''

'''Applicability
Use the Memento pattern when you want to produce snapshots of the object’s state to be able to restore a previous state of the object.

The Memento pattern lets you make full copies of an object’s state, including private fields, and store them separately from the object. While most people remember this pattern thanks to the “undo” use case, it’s also indispensable when dealing with transactions (i.e., if you need to roll back an operation on error).

Use the pattern when direct access to the object’s fields/getters/setters violates its encapsulation.

The Memento makes the object itself responsible for creating a snapshot of its state. No other object can read the snapshot, making the original object’s state data safe and secure.'''



''' The classic implementation relies on support for nested classes
    # can produce snapshots of its own state, 
    # can restore its state from snapshots.
    class Originator
        state
        save(): Memento
        restore(m: Memento): 

        # nested class, snapshot of the originator’s state
        class Memento
            state
            Memento(state) 
            getState() 
            # make the memento immutable

    class CareTaker
        originator
聚合     history: memento[]

        # has limited access to the memento’s fields and methods
        # pass memento object to originator
        doSomething(){  # ????? why not backup???
            m = originator.save()
            history.push(m)
        }
        undo(){
            m = history.pop
            originator.resotre(m)
        }

    到底 是CareTaker執行動作 還是 Originator執行動作?
'''

'''Implementation based on an intermediate interface
suitable for programming languages that don’t support nested classes

'''

'''Implementation with even stricter encapsulation
when you don’t want to leave even the slightest chance of other classes accessing the state of the originator through the memento.

'''

from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters


class Originator:
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


    def do_something(self) -> None:
        print("Originator: do something.")
        self._state = "".join(sample(ascii_letters, 11))
        print(f"Originator: my state has changed to: {self._state}")


class Memento(ABC):
    """
    provides a way to retrieve the memento's metadata,
    doesn't expose the Originator's state.
    """
    @abstractmethod
    def get_name(self) -> str:
        pass
    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        return self._state


    # just for Caretaker to display metadata.
    def get_date(self) -> str:
        return self._date
    def get_name(self) -> str:
        return f"{self._date} | ({self._state[0:9]}...)"


class Caretaker:
    """
    doesn't depend on the Concrete Memento class. 
        => doesn't have access to the originator's state, stored inside the memento. 
    """
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return
        memento = self._mementos.pop()

        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception: # TODO 不董
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


originator = Originator("Super-duper-super-puper-super.")
caretaker = Caretaker(originator)

caretaker.backup()
originator.do_something()

caretaker.backup()
originator.do_something()

caretaker.backup()
originator.do_something()

print()
caretaker.show_history()

print("\nClient: rollback one:")
caretaker.undo()

print("\nClient: rollback one:")
caretaker.undo()
