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
------------------------------------------------------------------
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
@abstractmethod->used to declare an abstract method and it is responsible to
enforce abstraction

Steps to make a class as an Abstract class and achieve abstraction

1)define a class that Should inherit ABC class
2)It shud contain Atleast 1 abtract method which shud be decorated using @abstractmethod
3)abstract class CANNot be Instantiated, we can create subclass instances using
  CONTRACT OF ABSTRACT.
4)CONTRACT OF ABSTRACT -> if a subclass inherits from abstract superclass, then
  the subclass MUST OVERRIDE all the abstract methods too create subclass instances
  Or else the subclass will also become an abtract class.

Concerte Class:
->Class that implements All the ingerited abstract methods or class that contain
  only concerte methods
->object creation for concreteclass is Allowed

Concerte Methods
->Methods that have complete implementation ans not decorated with @abstractmethod
->it can exist in abstract class and concrete class
->there is No Enforcement to overrife the methods



  



'''
