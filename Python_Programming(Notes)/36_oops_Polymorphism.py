'''
Polymorphism:
    -It is the ability of the single interface(method/operator) to perform different
     action depending on the object it is applied to.
    -In python, polymorphism allows same operator or method to behave differently
     depending on the object

    = > Polymorphism is implemented using 3 ways
      1)Method  Overriding
      2)Operator Overloading
      3)Ducktyping

1)Method Overriding:
  -It is a feature of inheritance where child class provides its own implementation
   for a method that is already defined in its parent class using the same method name
   and signature

   Syntax:
   class parentClass:
       def methodname(self):
           # parent method Implementation
    class ChildClass(ParentClass):#Inheritance(1)
        def methodname(self):     #Same methodname and parameter are parent method(2)
            #child method Implementation #Different Implemtation(3)

    obj=ChildClass()#Instantiation
    obj.methodname()

steps to showcase methodoverriding:
    1.1)Inheritance
    1.2)Method name of parent class and child class must be same
    1.3)No of parameters usually shud be same
    1.4)Implementation in the child method shud be changed

->It is also known as Runtime Polymorphism, Becoz the method which shud get
  executed is decided at runtime based on the actual object.

Super()
->super() is a built-in function that allowsa child class to call methods of its
  parent class(es). It's the proper way to access parent class functionality,
  especially whe you're overrifing methods.


Why do we need super()?

1)Retain & Reuse: It helps "retain/reuse existing functionality from the parent class
  "while having the flexibility to provide custom implementation in the child class
2)Avoid Code Repetition: Instead of rewriting parent class logic in the child,
  you can call the parent's implementation and add your own customizations.
3)Maintain Consistency: When overriding methods, super() ensures that the parent's
  initialization or behaviour is not lost.

  Syntax:
   from typing_extensions import override
   class parentClass:
       def methodname(self):
           #parent method Implementation
    class ChildClass(ParentClass):#Inheritance(1)
        @override #not mandatory, but good
        def methodname(self):     #Same methodname and parameter are parent method(2)
            super().methodname() #is calling the parent method implemtation
            #child method Implemtation
    obj=ChildClass()
    obj.methodname()

NOTE: 2 situation where we can use super
    1)method overriding
    2)Constructor chaining


"Constructor chaining"
    It is the process where in parent class constuctor is invoked/called from
    child class constructor using super()

    NOTE:
    1)super().__init() is used to "reuse/restore the common initialisation logic
      of the parent constructor/initialiser" from the child constructor, which
      reduces Repetition of Code and this is called as constructor chaining
      
    2)Defining a constuctor (__init__) in a child class will STOP the parent class
      constructor from being automatically called. The parent class attributes won't
      be initialized unless you "explicitly call super().__init__() from the child
      constructor

    3)super() doesnt just call the immedite parent, it follows the "method
      Resolution Order (MRO) in inheritence hierarchies, especially important
      in multiple inheritence.
    
    Syntax:
        class ParentClass:
            def _init_(self):
                #parent initialization logic #1

        class ChildClass(ParentClass):
            def _init_(self):
                super().__init__()
                #child initialization logic  #2

        c=ChildClass()

    Eg:
        class ParentClass:
            def _init_(self,a,b): #If parent constructor is having 'n' parameter
                #parent initialization logic #1

        class ChildClass(ParentClass):
            def _init_(self,a,b):
                super().__init__(a,b)#while calling super() in childconstructor
                                            pass (n-1) arguments 
                #child initialization logic  #2

        c=ChildClass(10,20)

object class:
    IN PYTHON every class automatically inherits from a built in class called
    object.
    -its the ultimate base class the root of python inheritance hierarchy.
    -even if you dont explicitly mention it, your classes inherit from object.

    -Importance of object class:
        the object clas provide a set of useful predefined special methods
        (dunder methods) that give "default behaviors to all objects", such
        as:
            -Printing/string representation
            -Comparison operations
            -hashing
            -Identity an type checking etc..

    -few important dunder methods are
        1).__new__(cls)
        2).__init__(self)
        3).__str__(self)
        4).__repr__(self)
        5).__hash__(self)
        6).__eq__(self,other)

    ----------------------------------------------------------------------
    1).__new__(cls):
        -it is used to create an actual instance of class.
        -it creates and returns the instance ans it is actually reponsible
         for instance creation.
        -it used object. __new__(cls) to allocate the memory location for
         the instance

         #eg:
             class Pen(object):
                 def __init__(self):
                     print("initialiser")

             p=Pen()---------------->(1)p=Pen.__new__(Pen) #empty pen instance
                        |                                  is created & return
                        |
                        |----------->(2)Pen.__init__(p) #constructor gets
                                                        executed.\


    2).__init__(self):
        -this methods gets automatically called only when we create an instance
         and is used to perform initialiser of instance.
        -to define initialiser in custom class, we need to have self as 1st
         implicit parameter.

    3).__str__(self):
        -this method gets invoked whenever an instance is printed or when called
         str(objectref).
        -and when called, by default it returns the string representation of the
         instance.
        -string representation is FullyQualifiedClassName
        @hexadecimal format:
        -we can override the __str__() to return a custom string representation
         useful/understandable to user

         NOTE:__str__ must always return a string.

         class ClassName(object):   #inheritance  (1)
             def __str__(self):     #methodname para same (2)
                 return "custom string"  #change the implementation (3)

         SYNTAX:
             def __str__(self):


    4).__repr__(self)
        -this method returns unambiguous(not confusing) developer representation
         of an object.
        -is used to define how an object should be represented as a string,
         mainly for developers during debugging, logging and development.
        -this method gets called
            1)when __str__() is absent and __repr__() is defined and when an
             instance is printed
            2)when we invoke repr(objectref)
            3)when we print containers(collection of objects)
        -and when called by default it returns the string representation of the
         instance (exactly samae as str).
        

5)__hash__(self)  ->
    ->this method gets invoked when we call hash(object) and bydefault returns
      a unique integer(hash value)
    ->hash value of an object is used in set and dictionary for quick searching
      and maintaining unique values(remove duplicates).
    ->default behaviour is to return a unique integer for each object
    ->NOTE: __hash__() must always return int

    Syntax:
        def __init__(self):
            #initialization Logic


        def __hash__(self):
            return uniqueinteger

        obj=ClassName()
        print(hash(obj)) #print(obj.__hash___())

6)__eq__(self,other);
    ->this method gets invoked/called when 2 instances are compared using == operator
      and By default it compares Identity (addresses) of 2 Instances, but NOT values.

    ->But in order to compare the values of custominstances rather that its addresses,
      we need to OVERRIDE __equ__()

    NOTE:->__equ__() is 'overriden' for the INBUILT types(int,float,list) etc

    ->this method shud always return a boolean (True/False)

    Syntax:
        Class ClassName:  #1
            def __init__(self):
                #initialization Logic

            def __eq__(self,other):
                return boolenvalue

        obj1=ClassName()
        obj2=ClassName()
        print(obj1==obj2) #print(obj1.__eq__(obj2))

    NOTE:
         isinstance(object, ClassName):
             ->its a predefined function that checks whethere the given object
               belongs to a particular class or not
             ->it returns boolean (True/False)
             
2)Operator Overloading:
    Operator overloading is the ability to change the behavior of an operator
    (like +, -, *, ==, <, etc.) so that it works with objects of user-defined
    classes. This is achieved by defining special methods, often called "dunder"
    (double underscore) methods, within those classes.

    ->Inbuilt classes=> Python's built-in classes like "int, float, str, and list
      "already have these dunder methods defined. When you use + with integers,
      Python knows to add them because the __add__ method is already there.
      
    ->User-Defined Classes:=›Python has no idea what" + or == "should mean for a custom class like Employee If you try to add two Employee objects without defining the behavior, Python will raise a TypeError.
      You must define the dunder methods to specify how the operators should
       behave.
    1)Arithmetic dunder methods
        -›used To define the behavior for mathematical operators like +,",*, 1,
            etc.
        -›When you use an operator, Python automatically calls the corresponding
          dunder method on the object on the left side of the operator.
        -›These methods must return a new object
        ->In the base object class, these methods are not defined. If you don't
          define them, your objects will not support these operators.
Operator        Dunder Method             Expression         Method Call
+               __add__(self,other)       a + b              a.__add__(b)
-               __sub__(self,other)       a - b              a.__sub__(b)
*               __mul__(self,other)       a * b              a.__mul__(b)
/               __truediv__(self,other)   a / b              a.__truediv__(b)
//              __floordiv__(self,other)  a // b             a.__floordiv__(b)
%               __mod__(self,other)       a % b              a.__mod__(b)
**              __pow__(self,other)       a ** b             a.__pow__(b)

2)Relational dunder methods:
    ->Used to define the behavior for comparison operators like ==, !=, <, >,
      <=, >=.
    ->Similar to arithmetic methos, the operator triggers the corresponding dunder
      method on the left hand object.
    ->These methods must return a Boolen value
    ->Just like the arithmetic ones, They are not defined in the base object class

-------------------------------------------------------------------------
 operator      Dunder method         expression           method call
-------------------------------------------------------------------------
   ==       __eq__(self,other)         a==b             a.__eq__(b)
   !=       __ne__(self,other)         a!=b             a.__ne__(b)
    <       __lt__(self,other)         a<b              a.__lt__(b)
    >       __gt__(self,other)         a>b              a.__gt__(b)
   <=       __le__(self,other)         a<=b             a.__le__(b)
   >=       __ge__(self,other)         a>=b             a.__ge__(b)
-------------------------------------------------------------------------


3)Duck Typing

Duck typing is a programming concept where the "type or class of an object" is
less important than the methods it defines. The name comes from the phrase:

"If it walks like a duck and quacks like a duck, then it must be a duck."

In Python, this means
->You don't care about "what an object is, you care about what it can do"
-›If an object has the required methods/attributes, it can be used in that context
-›Python "focuses on behavior rather than explicit type checking"
NOTE1):inheritance 1s NOT needed in Ducktyping
NOTE1)No need of any base class
Note3)No explicit type checking involved

hasattr(obj_ref, "attributename")
    ->its predefined function user to check if attribute(varible/method) is
      present/belongs to that object
    ->it returns boolean value
    ->it returns True if attibute is present in that object, else it returns False
'''