# https://refactoring.guru/design-patterns/abstract-factory
'''
produce families of related objects without specifying their concrete classes
'''

'''
    Abstract ProductA
繼承 ConcreteProdcutA1
繼承 ConcreteProdcutA2

    Abstract ProductB
繼承 ConcreteProdcutB1
繼承 ConcreteProdcutB2


    Interface [AbstractFactory]
        CreateProductA :[ProductA]
        CreateProductB :[ProductB]
實現 Class [ConcreteFactory1]
    覆寫 CreateProductA :[ProductA] return new ConcreteProductA1
    覆寫 CreateProductB :[ProductB] return new ConcreteProductB1
實現 Class [ConcreteFactory2]
    覆寫 CreateProductA :[ProductA] return new ConcreteProductA2
    覆寫 CreateProductB :[ProductB] return new ConcreteProductB2
'''
# 每個工廠 出一套[產品套]
# 產品矩陣   配件1 配件2

# 風格1
# 風格2

# 一個風格交給一個工廠

from abc import ABC, abstractmethod

class AbstractProductA(ABC):
    pass
class ConcreteProductA1(AbstractProductA):
    pass
class ConcreteProductA2(AbstractProductA):
    pass

class AbstractProductB(ABC):
    pass
class ConcreteProductB1(AbstractProductB):
    pass
class ConcreteProductB2(AbstractProductB):
    pass




class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()
    

def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

client_code(ConcreteFactory1())
client_code(ConcreteFactory2())