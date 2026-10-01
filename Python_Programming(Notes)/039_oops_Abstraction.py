'''
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
Abstraction:
    -important oops principle, which is the process of "defininf required behaviour
     in parent class without providing full implementation and forcing the subclass
     to implement it".
----------------------------------------------------------------
Abstract class(Incomplete class)
    ->It is a class that is meant ONLY for inheritance, becoz it CANNOT be
      Instantiated(onkect creation is NOT possible,)
    ->abstract class is a idea/concept and is incomplete by design.
    ->shud have atleast 1 "abstract method".
    NOTE:
    abstract class acts like a contract, which ENFORCES the rules upon subclasses
\------------------------------------------------------------------
abstract method->It is method declared in abtract class decorated using
                 @abstractmethod
               ->Is an incomplete method, having method name and parameter, BUT
                 NO Implementation
               ->it is meant to be overriden/implemented by the child classes
Syntax:

from abc import ABC, abstractmethod
class ClassName(ABC):
    @abstractmethod
    def methodname(self): #abstractmethod
        pass              #incomplete implementation
Note:
abc=>abtract base classes, is a module in python used to support abstraction

ABC=>abstract base class, is a class imported from abc module, which is used as baseclass to create abstract classes
@abstractmethod->used to declare an abstract method and it is responsible to enforce abstraction
'''