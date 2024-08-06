'''
solves two problems: # violating the Single Responsibility Principle:
    ensure that a class has only one instance
    providing a global access point to this instance.
        global variables : 
            very unsafe since any code can potentially overwrite the contents of those variables and crash the app


It may be difficult to unit test the client code of the Singleton because many test frameworks rely on inheritance when producing mock objects.
'''
'''
Make the default constructor private, 

Create a static creation method 
    calls the private constructor to create an object
    saves it in a static field. 
    All following calls to this method return the cached object.
'''

'''
    class Singleton
        private static instance :Singleton 

        private Singleton() 
        public static getInstance() :Singleton {
            if instance is null{
                intance = new Singleton()
            }
            return instance
        }


'''



class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. 
    Some ossible methods include: 
        base class, 
        decorator, 
        metaclass. 
    We will use the metaclass because it is best suited for this purpose.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print( id(cls))
        print(cls._instances)
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):
    pass

s1 = Singleton()
s2 = Singleton()
if id(s1) == id(s2):
    print("Singleton works")