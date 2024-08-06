from __future__ import annotations
'''
define a subscription mechanism to notify multiple objects about events that happen to the observed object.
'''

'''Applicability
when changes to the state of one object may require changing other objects, 
and the actual set of objects is unknown beforehand or changes dynamically.
'''

'''
client
    s = new ConcreteSubscriber()
    publisher.subscribe(s)
---------------------------
    class Publisher             #issues events, notify Subscribers
聚合     subscribers: Subscriber[]
        mainState

        subscribe(s:Subscriber)
        unsubscribe(s:Subscriber)
        notifySubscribers(){
            foreach( s in subscribers){
                s.update(this)
            }
        }
        mainBusinessLogic(){
            mainState = newState
            notifySubscribes()
        }


    Interface Subscriber
        update(context) 
            #may have parameters for publisher to pass event details

實現 class ConcreteSubscribers
        update(context)
'''


from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    '''
    publisher
    '''
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):
    _state: int = None
    _observers: List[Observer] = []
    """
    List of subscribers.
    subscribers can be stored more comprehensively 
    (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        print("\nSubject: doing something.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()



class Observer(ABC):
    """
    Subscriber Interface
    """
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        print("ConcreteObserverB: Reacted to the event")



subject = ConcreteSubject()

observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()
subject.attach(observer_a)
subject.attach(observer_b)

subject.some_business_logic()

subject.detach(observer_a)

subject.some_business_logic()
