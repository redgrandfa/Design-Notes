from __future__ import annotations
'''
traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

extract the traversal behavior of a collection into a separate object called an iterator
'''

'''Applicability
when your collection has a complex data structure, but you want to hide its complexity from clients (for convenience or security).

reduce duplication of the traversal code across your app.

when you want your code to be able to traverse different data structures or when types of these structures are unknown beforehand.
'''

'''

client

    #declares the operations required for traversing a collection
    Interface Iterator 
        getNext()
        hasMore():bool

    # declares one or multiple methods for getting iterators compatible with the collection
    Interface IterableCollection
依賴    createIterator(): Iterator



實現 class ConcreteIterator
        collection: ConcreteCollection
        iterationState

        ConcreteIterator( c: ConcreteCollection )

        getNext()
        hasMore():bool

互相關聯

實現 class ConcreteCollection
        createIterator(): Iterator
        ...(other detail being a collection )

'''

from collections.abc import Iterable, Iterator
from typing import Any


"""
in Python, there are two abstract classes from the built-in `collections` module
implement:
    `__iter__()` method in the Iterable
    `__next__()` method in the iterator
"""


class AlphabeticalOrderIterator(Iterator):
    """
    implement various traversal algorithms.
    store the current traversal position at all times.
    """

    """
    `_position` attribute stores the current traversal position. 
    may have a lot of other fields for storing iteration state
    """
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any:
        """
        either return next item
        or raise StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    """
    Concrete Collections provide methods for retrieving fresh
    iterator instances, compatible with the collection class.
    """

    def __init__(self, collection: list[Any] | None = None) -> None:
        self._collection = collection or []

    def __getitem__(self, index: int) -> Any:
        return self._collection[index]
    
    def add_item(self, item: Any) -> None:
        self._collection.append(item)

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self, True)




collection = WordsCollection()
collection.add_item("First")
collection.add_item("Second")
collection.add_item("Third")

print("Straight traversal:")
print("\n".join(collection))
print("")

print("Reverse traversal:")
print("\n".join(collection.get_reverse_iterator()), end="")
