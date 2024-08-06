# https://refactoring.guru/design-patterns/factory-method
'''
彈性適應不同instance (稱為 products)，包含未來擴充的

replace direct object construction calls (using the new operator) with calls to a special factory method

子類可override 此方法
'''
'''
(client code) doesn’t see a difference between the actual products returned by various subclasses. (product as interface-type varibale)

'''

'''
    Interface [Product]
實現 class Prod_1
實現 class Prod_2

        #Creator 依賴 Product

    BaseClass [Creator]
工廠方法 [Product] CreateProdcut() 
繼承 class Creator_1
    覆寫 [Product] CreateProdcut() :  return new Prod_1()
繼承 class Creator_2
    覆寫 [Product] CreateProdcut() :  return new Prod_2()

    切換Creator以取得不同Product instance
    client code 只知道獲得一個 Product型別變數

'''

from abc import ABC, abstractmethod

class Product(ABC):
    def operation(self) -> str:
        pass

class ConcreatProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        # default behavior
        pass
    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        """
        product = self.factory_method()
        result = f"Creator: product: {product.operation()}"
        return result
    
class ConcreatCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreatProduct1()
    

def client_code(creator:Creator)-> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
        f"{creator.some_operation()}")

client_code(ConcreatCreator1())
# client_code(ConcreatCreator2())


# 時機
# don’t know beforehand the exact types and dependencies of the objects 

# constructor can only new object, can't reuse existing instances


'''如何實踐
find all references to product constructors. 
    replace them with calls to the factory method

此時 可能Creator中有大量條件判斷 > 使用多型
create a set of creator subclasses for each type of product


Single Responsibility Principle.
Open/Closed Principle
'''


# https://refactoring.guru/design-patterns/factory-comparison

