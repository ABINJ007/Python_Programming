'''

Application Programming Interface:
----------------------------------
-It acts as intermediate medium between 2 or more applications
-It is a Contract that defines HOW a client CAN ACCESS A Service, without knowing
 How the service is implemented
-"Abstract class" helps us design such API contracts

Tight Coupling:
--------------
-If a change in service provider forces the user to make changes in client side,
 then it is case of tight coupling
-Tight coupling is bad design principle becoz it expects the client code to
 change each time
-The service provider changes, therefore to avoid this we need to achieve Loose
 coupling through API(ie, abstract classes).


Loose Coupling:
    If a change in service provider does NOT force the user/client code to make
    changes, then it is a case of loose coupling.
    
    Loose coupling is a good design principle because it allows the client code
    to remain unchanged even when the service privider changes. This is achieved
    by making the client depend on an API(i.e an abstract class rather than
    directly depending on a particular service providers.
'''
     







