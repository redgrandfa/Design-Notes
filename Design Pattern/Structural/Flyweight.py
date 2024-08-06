"""
save memory by sharing common parts of state between multiple objects instead of keeping all of the data in each object.

make sure your program does have the RAM consumption problem 
    related to having a massive number of similar objects
Make sure that this problem can’t be solved in any other meaningful way.
"""
"""
an object that only stores the intrinsic state is called a flyweight.

"""

# Extrinsic state storage

"""
    cleint
組合 class Context
        extrinsicState|unique 他自己的獨特資訊
        flyweight  -> 指向他該有的共同資訊

        Context( intrinsicState, extrinsicState )
        operation(){
            flyweight.operation( extrinsicState) #補給他獨特資訊
        }

        
    class FlyweightFactory
聚合     cache : Flyweight[]
        getFlyweight(intrinsicState)

    class Flyweight
        intrinsicState|Shared
        operation( extrinsicState )  #拿獨特資訊

"""


import json
from typing import Dict


class Flyweight:
    # stores intrinsic state
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    # accepts extrinsic state via method parameters.
    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")


class FlyweightFactory:
    """
    creates and manages the Flyweight objects.
    ensures that flyweights are shared correctly.
    When the client requests a flyweight, 
        returns an existing instance or creates a new one
    """

    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: creating new flyweight.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        print(f"FlyweightFactory: I have {len(self._flyweights)} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_car_to_police_database(
    factory: FlyweightFactory,
    plates: str,
    owner: str,
    brand: str,
    model: str,
    color: str,
) -> None:
    print("\n\nClient: Adding one to database.")
    # search|create flyweight by intrinsic state 
    flyweight = factory.get_flyweight([brand, model, color])
    # pass extrinsic state to the flyweight's methods.
    flyweight.operation([plates, owner])


factory = FlyweightFactory(
    [
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ]
)
# factory.list_flyweights()
add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "M5", "red")
add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "X1", "red")

print("\n")
factory.list_flyweights()
