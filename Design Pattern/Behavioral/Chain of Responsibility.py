from __future__ import annotations

'''
pass requests along a chain of handlers. 
    each handler decides either 
        to process the request 
            or 
        to pass it to the next handler
'''

'''
    client
        h = new HandlerA( new HandlerB() )
        h.handle(request)

    interface Handler
        setNext(h: Handler)
        handle(request)

    class BaseHandler
        next: Handler
        setNext(h: Handler)
        handle(request){
            # 傳遞
            if (next != null){ next.handle(request) }
        }

    class ConcreteHandlers
覆寫     handle(request){
            if ( canHandle(request) ){ ... } 
            else{ 
                # 統一呼叫基底類handle傳給下一位
                parent::handle(request) 
            }  
        }   
'''
# Note that a request can be sent to any handler in the chain
#   it doesn’t have to be the first one.

'''Applicability
- expected to process different kinds of requests in various ways, but the exact types of requests and their sequences are unknown beforehand.


- to execute several handlers in a particular order.

- when the set of handlers and their order are supposed to change at runtime.
    If you provide setters for a reference field inside the handler classes, you’ll be able to insert, remove or reorder handlers dynamically.
'''

from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass
    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler
        # Returning a handler from here will let us link handlers in a convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
All Concrete Handlers 
"""
class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is not even aware that the handler is part of a chain.
    """

    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")


monkey = MonkeyHandler()
squirrel = SquirrelHandler()
dog = DogHandler()

monkey.set_next(squirrel).set_next(dog)

# able to send a request to any handler, not just the
# first one in the chain.
print("Chain: Monkey > Squirrel > Dog")
client_code(monkey)
print("\n")

print("Subchain: Squirrel > Dog")
client_code(squirrel)
