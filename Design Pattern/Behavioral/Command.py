'''
turns a request into a stand-alone object that contains all information about the request. 
This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.
'''

'''problem
ex. a button UI with different functionality, 
    declare new subclass => too much subclasses
'''


'''sol
principle of separation of concerns

    GUI layer
    business layer

The GUI objects may access the business logic objects directly.

The Command pattern suggests that 
    GUI objects shouldn’t send these requests directly. 
    Instead, you should extract all of the request details, 
        such as the object being called, the name of the method and the list of arguments 
    into a separate command class with a single method that triggers this request.

    the GUI object doesn’t need to know what business logic object will receive the request and how it’ll be processed. 
    
    The GUI object just triggers the command, which handles all the details.

    put a single field into the base Button class that stores a reference to a command object


    commands become a middle layer that reduces coupling between the GUI and business logic layers
'''

'''Applicability
when you want to parametrize objects with operations.

when you want to queue operations, schedule their execution, or execute them remotely

when you want to implement reversible operations.
    Although there aremany ways to implement undo/redo, the Command pattern is perhaps the most popular of all.
    
    The command history is a stack

    it isn’t that easy to save an application’s state because some of it can be private. 
    This problem can be mitigated with the Memento pattern.
''' 

# V Single Responsibility Principle. 
#   decouple
# V Open/Closed Principle. 
#   introduce new commands into the app
# V can assemble a set of simple commands into a complex one.

# X more complicated since introducing 
#   a whole new layer between senders and receivers

'''
client
    copy = new CopyCommand(editor)
    button.setCommand(copy)


    Class Invoker    # or call Sender
關聯     command: Command
        setCommand(command)
        executeCommand()


關聯 Interface Command
        execute()

實現 class ConcreteCommand1
關聯     receiver : Receiver
        params
        ConcreteCommand1(receiver, params)

        execute(){ # pass the call to one of the business logic objects
            receiver.operation(params)
        }

    # business logic objects
關聯 Class Receiver
        operation(params)
'''
# from __future__ import annotations
from abc import ABC, abstractmethod

class Receiver:
    """
    business logic.
    """
    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


# A command implement simple operations on their own.
class SimpleCommand(Command):

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: do simple things:" f"({self._payload})")

# A command delegate more complex operations to other
# objects, called "receivers."
class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, a: str) -> None:
        """
        Complex commands can accept one or several receiver objects along with
        any context data via the constructor.
        """

        self._receiver = receiver
        self._a = a

    def execute(self) -> None:
        """
        delegate to a receiver.
        """

        print("ComplexCommand: delegate to a receiver ", end="")
        self._receiver.do_something(self._a)



class Invoker:
    """
    associated with one or several commands
    sends a request to the command.
    """

    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        not depend on concrete command or receiver classes. 
        Invoker passes a request to a receiver indirectly, by executing a command.
        """

        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...I do something...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()

invoker = Invoker()
invoker.set_on_start(SimpleCommand("Say Hi!"))
receiver = Receiver()
invoker.set_on_finish(ComplexCommand(
    receiver, "Send email"))

invoker.do_something_important()
