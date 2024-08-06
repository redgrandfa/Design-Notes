from __future__ import annotations
'''
lets an object alter its behavior when its internal state changes. 
It appears as if the object changed its class.
'''

'''
finite number of states
program can be switched from one state to another instantaneously.
depending on a current state, the program may or may not switch to certain other states.
switching rules, called transitions, are also finite and predetermined.

'''
'''
State pattern suggests that you 
    create new classes for all possible states of an object 
    and 
    extract all state-specific behaviors into these classes.
'''

'''Applicability
when you have an object that behaves differently depending on its current state, 
    the number of states is enormous, 
    and the state-specific code changes frequently.

when you have a class polluted with massive conditionals that alter how the class behaves according to the current values of the class’s fields.

when you have a lot of duplicate code across similar states and transitions of a condition-based state machine.
'''



'''
client
    initailState = new ConcreteState()
    context = new Context(initialState)
    context.doSth()


    class Context
聚合     state
        Context(initialState){
            this.State = state
            state.setContext(this)
        }
        changeState(state)
        doSth(){  
            #delegate the 'state-related' behavior to state object
            state.doSth()
        }

    Interface State
        doSth()

    class ConcreteStates
        context
        setContext(context)
        doSth(){
            ...logic...

            # a state may change state in context
            state = new OtherState()
            context.changeState(state)
        }

        


'''


from abc import ABC, abstractmethod


class Context:
    _state = None
    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        allows changing the State object at runtime.
        """
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    delegates part of its behavior to the State object.
    """

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
    provides a backreference to the Context object,
    backreference can be used to transition the Context to another State.
    """
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())


# The client code.

context = Context(ConcreteStateA())
context.request1()
context.request2()
