'''
lets you provide a substitute or placeholder for another object. 
'''


'''Applicability

Lazy initialization (virtual proxy). 
    when you have a heavyweight service object that wastes system resources by being always up, 
    delay the object’s initialization to a time when it’s really needed.

    In an ideal world,  we’d want to put this code directly into our object’s class, 
        but that isn’t always possible. (may be part of a closed 3rd-party library.)


Access control (protection proxy). 
    when you want only specific clients to be able to use the service object; 
    The proxy can pass the request to the service object 
        only if the client’s credentials match some criteria.

        
Local execution of a remote service (remote proxy). 
    This is when the service object is located on a remote server.
    In this case, the proxy passes the client request over the network


Logging requests (logging proxy). 
    The proxy can log each request before passing it to the service.

    
Caching request results (caching proxy). 
    The proxy can cache results of client requests and manage the life cycle of this cache,
    may use the parameters of requests as the cache keys.

    
Smart reference. 
    The proxy can keep track of clients that obtained a reference to the service object or its results. 
    From time to time, the proxy may go over the clients and check whether they are still active. 
    If the client list gets empty, the proxy might dismiss the service object and free the underlying system resources.

    The proxy can also track whether the client had modified the service object. 
        Then the unchanged objects may be reused by other clients.

'''

'''
The proxy works even if the service object isn’t ready or is not available.

Open/Closed Principle. You can introduce new proxies without changing the service or clients.
'''

'''
    client

    Interface ServiceInterface
        operation()

實現 class Service
        operation()

實現 class Proxy  
        realService: Service

        Proxy(s: Service) { realService = s }
        checkAccess()
        operation(){   # delegate work to the real one
            if( checkAccess() ){    
                realService.operation()
            }
        }
'''

from abc import ABC, abstractmethod


class Subject(ABC):
    """
    common interface of both
    declares common operations for both Real-One and the Proxy. 
    """

    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: Handling request.")

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.extra()

    def check_access(self) -> bool:
        print("Proxy: Checking access before firing a real request.")
        return True

    def extra(self) -> None:
        print("Proxy: extra")


def client_code(subject: Subject) -> None:
    subject.request()


print("\tClient: Executing the client code with a real subject:")
real_subject = RealSubject()
client_code(real_subject)

print("")
print("\tClient: Executing the client code with a proxy:")
client_code( Proxy(real_subject) )
