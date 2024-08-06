'''
allows objects with incompatible interfaces to collaborate
'''

'''1. Object adapter
    {client code}   #doesn’t get coupled to the concrete adapter class

關聯 Interface ClientInterface
        method(data)

實現 Class Adapter          #converter between 
        adapee: Service     #wrapping the service object
    實現 method(data){
            specialData = convertToServiceFormat(data)
            return adaptee.serviceMethod(specialData)
        }

關聯 Class Service (#usually 3rd-party or legacy)
        serviceMethod(specialData)
    
'''

'''2. Class adapter 
# need  programming languages(such as C++) support multiple inheritance


    Class Adapter    
        (inherit ClientInterface)
        (inherit Class Service)
        method(data){
            specialData = convertTo...
            return this.serviceMethod(specialData)
        }
'''

'''
Single Responsibility Principle. 
    separate data conversion code
Open/Closed Principle. 
    introduce new types of adapters without breaking the existing client code
'''

'''
complexity increases 
    introduce a set of new interfaces and classes. 
Sometimes it’s simpler just to change the service class
'''
def client_code(target: "Target") -> None:
    print(target.request(), end="")


class Target:
    def request(self) -> str:
        return "Target: default"
    
class Adaptee: # Service 
    '''
    incompatible with the existing client code
    '''
    def specific_request(self) -> str:
        return "laicepS :eetpadA"

class Adapter(Target, Adaptee): # via multiple inheritance.
    """
    makes the Adaptee compatible with the Target's interface 
    """
    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"



print("Client: I can work just fine with the Target objects:")
client_code( Target() )
print("\n")

print("Client: The Adaptee class has a weird interface. "
        "I don't understand:")
print(f"Adaptee: { Adaptee().specific_request()}", end="\n\n")

print("Client: But I can work with it via the Adapter:")
client_code( Adapter() )