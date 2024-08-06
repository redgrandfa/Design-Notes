'''簡化窗口
provides a simplified interface to a library, a framework, or any other complex set of classes.
'''

'''
A facade might provide limited functionality in 
    comparison to working with the subsystem directly. 
'''



'''
    client

class Facade
依賴 - links To Subsystem Objects
依賴 - optional Additional Facade
    - subsystemOperation()      
    # delegates the client requests to the appropriate subsystem


class AdditionalFacade

'''


# The Subsystem can accept requests either from the facade or client directly.
class Subsystem1:
    def operation1(self) -> str:
        return "Subsystem1: Ready!"
    def operation_n(self) -> str:
        return "Subsystem1: Go!"


class Subsystem2:
    def operation1(self) -> str:
        return "Subsystem2: Get ready!"
    def operation_z(self) -> str:
        return "Subsystem2: Fire!"


class Facade:
    """
    delegates the client requests to the appropriate subsystem. 
    also responsible for managing their lifecycle.
    shields the client from the undesired complexity of the subsystem.
    """

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        """
        can provide the Facade with existing subsystem objects 
        or 
        create them on its own.
        """
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        """
        The Facade's methods are convenient 
        but clients get only to a fraction of a subsystem's capabilities.
        """

        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)



def client_code(facade: Facade) -> None:
    print(facade.operation(), end="")


subsystem1 = Subsystem1()
subsystem2 = Subsystem2()
facade = Facade(subsystem1, subsystem2)
client_code(facade)

