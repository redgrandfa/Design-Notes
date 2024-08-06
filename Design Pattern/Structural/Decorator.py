"""
lets you attach new behaviors to objects 
    by placing these objects inside 
        special wrapper objects that contain the behaviors.
"""

"""
need to alter an object’s behavior.
Inheritance is static. 
    can only replace the object with another one 
        created from a different subclass.

        
problem: multiple inheritance allowed?
=> by using Aggregation or Composition  instead of Inheritance.
"""

"""
The wrapper contains the same set of methods as the target and delegates to it all requests it receives. 
"""


# The last decorator in the stack would be the object that the client actually works with

"""
    client{
        a = new ConcreteComponent()
        b = new ConcreteDecorator1(a)
        c = new ConcreteDecorator2(b)
        c.execute() 
    }

    # common interface for both wrappers and wrapped objects.
    Interface IComponent
        execute()

    # defines the basic behavior, which can be altered by decorators.
實現 Class ConcreteComponent   
        execute()

實現 Class BaseDecorator
關聯?聚合?wrappee: Component  
        BaseDecorator(c: Component) { wrappee = c}
        execute() { wrappee.execute() }
        # 這形成stack的作用! 我.execute()其實是delegate給wrappee.execute

繼承 Class ConcreteDecorators
        execute(){ 
            before() # 額外的Decorate
            supuer::execute() 
            after()   # 額外的Decorate
        }  
        before()
        after()

"""

'''sample:  我覺得有點像Pipeline
                Decor1   Decor2
    clinet -> Encrypt -> compress  -> datasource 
    clinet <- decode -> decompress -> datasource 
'''

'''Use the pattern 
#   not possible to extend an object’s behavior using inheritance.
  change behaviors of objects at runtime
      add | remove | combine

 Seperate Responsibility 
'''
'''
X hard to remove a specific wrapper from the wrappers stack.
X hard to implement a decorator in such a way that its behavior doesn’t depend on the order in the decorators stack.


'''

class Component():
    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    _component: Component = None #wrappee

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self) -> str: #delegate to wrappee
        return f"ConcreteDecoratorA({self.component.operation()})"

class ConcreteDecoratorB(Decorator):
    def operation(self) -> str: #delegate to wrappee
        return f"ConcreteDecoratorB({self.component.operation()})"


def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")



simple = ConcreteComponent()
decorator1 = ConcreteDecoratorA(simple)
decorator2 = ConcreteDecoratorB(decorator1)
client_code(decorator2)

