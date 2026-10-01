'''

OOPS
-> IN python, we can write program without class, but real time large scale project oops in needed

->based on 2 concepts and 4 principles
1)class
2)object/instance

4 principles
1)Encapsulation
2)Inheritance
3)Polymorphism
4)Abstraction

object-oriented:
    ->representign everything in prog in the form of objects that store data(states) and perform actions (behaviours)
    ->python treates almost everything as an object(numbers,str,list,func etc)

Class->Blueprint/logicalentity(template), tthat describes the property and behaviour of an object
     ->class define states represent using variables
     ->behaviour represents using method

     syntax  for userdefined class=>
         class ClassName:
             pass

        obj = ClassName() #One class N number of objects
===========================================
object->Instance of a class
    ->it repre real world(student,employee,account) or logical entity(int,list,str obj) that has state and behaviour
    instantiation->process of creating instance of a class
    ->note:to create an object, class must be created first
    syntax:
        instancereference=ClassName()

    ->using on class -> we can create multiple instance and each instance is independent entity
    ->changes made to 1 instance  does not affect other instance.

    ========================================
    Memory Allocation wrt Class and Instances
    -----------------------------------------
        ->when class is defined, class dictionary get created and insider it variable and methods of that class is stores in the form of key and values

        ->When instance is createdm instance dictionary gets created and inside it instance data is stored in the form of key and values, it will have a reference to class.

        Note: print(ClassName.__dict__)  #displays the Class dictionary
              print(objreference.__dict__) #displays the instance dictionary
=======================================================================

variables wrt class and object scope
------------------------------------
1)class variables
2)instance variables

1)->class variables defined inside a class but outside all methods
syntax:
    class ClassName:
            variable_name=value
 -outside the class, it can be defined using the ClassName,
    syntax:
        ClassName.variablename=value
 -only 1 copy of class variables for entire calss and it is not tied to any single instance
 ->All class variables are stored inside class dictionary
 -if any value is common for all instances, it shud be made as classvariable
 -how to access a class variable
        ->ClassName.variablename
        ->instanceref.variablename
 -MOdification of class variable willaffect all the instance
        ->ClassName.variablename=newvalue,

2)instance variables->variables declared/defined using instance reference
    ->instance creation is mandatory to declare instance variables.
    Syntax:
        instance_reference.variable_name=value
    ->one copy for each instance, created separately for each instance
    ->if a variable is unique for each object, only then make it as a instance
      variable
    ->instance variable are stored inside instance dictionary
    ->we can ACCESS and MODIFY an instance variable
        accessing=>using instanceref.variablename
        modifying=>instanceref.variablename=newvalue
    ->modifying instance variables will  affect only that specific instance
============================================================================
Contructor/Initialiser->
    -It is a block of code /special dunder method used to declare and
      initialize instance variables of an instance
    -Syntax:
        class ClassName:
            def __init__(self):#<-Initializer/constructor gets executed every
                                time an instance is created
                #Initialisation


        objref=ClassName()     
        -the constructor/Initializer must be written within the class and its name should be __init__(self)
        -self must be the 1st implicit parameter in the constructor and it refers to the current invoking instance
        -using self parameter inside the constructor, we create and initialise instance variables using syntax
                ->self.variablename=value

        -instance creation is compulsory in order to execute initializer/constructor
        -If there are n parameters in the constructor, we need to pass n-1 arguments during the instance creation/constructor call

                      Initializer/Constructor
                                 |
                -----------------------------------------
            DefaultContructor              UserDefined Constructor
                                                    |
                                    ----------------------------------
                                  CNPC                               CPC
             

Creation/Constructor call:
--------------------------
Types of Constructor:
    1)Default constructor
        -it will not be visible to the user
        -this will be present in the super class object
        -when the user does not provide custom constructor default constructor will be user during instance creation
    2)Custom Custructor
        -A constructor/Initializer explicitly defined by the programmer insider the class is called a custom constructor
        2.1)Custom nonparameterised constructor
            -It has only seld as a parameter.
            -used when no external values need to be passed during object creation

        2.2)Custom parameterised constructor
            -An initializer that has self plus one or more additional parameters
            -If total no of parameters is n, the user shud pass n-1 no of argumetns during the object
             creation(constructor call)
=======================================================================
Methods=>Any Function defined inside a class, Based on how methods work with
         instances and class, 3 types.
         1)Class methods
         2)instance methods
         3)static methods

         1)class methods:
            ->which belongs to the class itself , not to the instance
            ->This methof works on class level data and not on instance
            ->it receives the class reference as the 1st parameter refered to
              class
            ->class method id declared using @classmethod decorator just above
              the method
            Syntax:
                class ClassName:
                    @classmethod
                    def method_name(cls,para1,para2):
                        #classmethod body/logic
                ClassName.methodname(arg1,arg2...)
                
            ->If there are "n" parameters in the class method, we shud pass "n-1" arguments
              during the class method calling
            ->A class methof can ACCESS and MODIFY the class variables
            ->accessing a class method using ClassName.classmethod()
            ->when an operation is related to a class and a particular instance we
              use class methods.
2)Instance methods:
    ->which belongs to the instance
    ->this method works on instance specific data
    ->it receives the current instance reference as the 1st parameter referred to self
    Syntax:
        class ClassName:
            def method_name(self,para1,para2,......):
                #method body/logic
        reference=ClassName()
        reference.method_name(arg1,args,...)

    ->if there are "n" parameters in the instance method, we shud pass "n-1" arguments
      during the instance method calling
    ->A instance method can ACESS and MODIFY the instance variables
    ->accessing a instance method using
            instanceref.instancemethodname()
    ->when an operator is related to particular instance we use instance methods.
3)Static methods
    ->DO NOT depend on class or instance
    ->this method does NOT operate on class or instance data
    ->it DOES NOT receive self or cls as the 1st parameter
    ->it shud be defined using @staticmethof decorator above that method
    Syntax:
        class ClassName:

            @staticmethod
            def method_name(para1,para2,....):
                #method body/logic
        ClassName.method_name(arg1,arg2,....):#can call using classname
        reference=ClassName()
        reference.method_name(arg1,arg2,....):#call call usign instance ref

    ->if n parameter are present in the static method n arguments has to be passed
      while calling static method
    ->A static method can be called or invoked using ClassName or instance reference
    ->it behaves like a normal function, but it is used when logic is related to class
      (for logical grouping purpose)->helper class utility method

Advantages of Methods:
1)Enforce a logic before changing data
2)Avoids Cod Duplication
3)Adheres principles of OOPS
4)it allows abstraction

Inheritance:
------------
The process of 1 class acquiring the properties of another calss
    ->The class which shares the properties->parent or super or base class
    ->The class which acquires the properties->child or sub or derived class
    ->Inheritance can be referred to as 'IS -A -Relationship'
    ->In python we can inherit variables and methods

Types of Inheritance:

1)Single Level
2)Multi Level
3)Heirarchical Level
4)Multiple Level
5)Hybrid Inheritance

1)Single level
      -----
      | A |
      -----
        ^
        |
        |
      -----  
      | B |
      -----
Class A: #parent class
    ->A states
      A Behaviours
Class B(A):  #child class
    ->B class states
    ->B class behaviours

1)single Level-.combination of 1 suberclass and 1 subclass

NOTE:
    MRO->Method resolution Order
    ->It is a method order in which python searches classes to find that method
    ->This is releveant only when there is more tha 1 inheritance path
    ->ClassName.__mro__

2)Multi-Level->Combination of 2 or more singlelevel inheritance in a sequential
               Manner
      -----
      | A |
      -----
        ^
        |   
        |
      -----  
      | B |
      -----
        ^
        |
        |
      -----  
      | C |
      -----
Class A: #parent class
    ->A states
      A Behaviours
Class B(A):  #child class
    ->B class states
    ->B class behaviours
Class C(B):  #GC
    ->C class states
    ->C class behaviours
    
3)Heirarchical->1 super class having 2 or more subclasses
        -----
        | A |
        -----
     /    ^   \
    /     |    \
   /      |     \
 -----  -----  -----
 | B |  | C |  | D |
 -----  -----  -----
Class A: #parent class
    ->A states
    ->A Behaviours
Class B(A):  #child class
    ->B class states
    ->B class behaviours
Class C(A):  #child class
    ->C class states
    ->C class behaviours

Class D(A)   #child class
    ->C class states
    ->C class behaviours
    
4)Multiple-> One childclass have same attribute name or method classes.
NOTE=> if both the superclasses have same attribute name or method name, based upon
       the mro(method resolution order) the method present in the immediate superclass
       will be executed
       

Class A: #parent class
    ->A states
    ->A Behaviours
Class B:  # parent class
    ->B class states
    ->B class behaviours
Class C(A,B):  #child class
    ->C class states
    ->C class behaviours
 -----       -----  
 | A |       | B |  
 -----       -----
       \   /
        \ /
       -----
       | C |
       -----
              
5)Hybrid Inheritance:
    ->Combination of 2 or more different inheritance types

Advantages->
1)Code Reusability->Reuses code of present class instead of rewritting in child class
2)Logical class Hierarchy->code will be in structured and heirarchical manner
3)Extensibity->child class can override the methods of parent class to give new functionality

       -----                
       | A |
       -----
     /        \
    /          \
   v           v
 -----       -----  
 | B |       | C |  
 ----- ^   ^ -----
       \   /
        \ /
       -----
       | D |
       -----
Class A: #parent class
    ->A states
    ->A Behaviours
Class B(A):  #child class
    ->B class states
    ->B class behaviours
Class C(A):  #child class
    ->C class states
    ->C class behaviours

Class D(B,C)   #GC
    ->C class states
    ->C class behaviours
    
Polymorphism:
    -It is the ability of the single interface(method/operator) to perform different
     action depending on the object it is applied to.
    -In python,polymorphism allows same operator or method to behave differently
     depending on the object

    =>Polymorphism is implemented using 3 ways
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
           #parent method Implementation
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

AccessSpecifiers/Modifiers:
    ->It applies only inside classes, a because classes are about encapsulation
    ->these are used to specify the visibility or accessibility of variables or
      methods
3Types
1)Public
2)Protected
3)Private

1)Public:
    ->any var or method declared normally inside a class is by default considered
     as public
    ->No leading underscore are used for it
    ->such var or methods can be accessed from anywhere(from inside class or from
      outside class in samemodule or outside module in samepackage)

2)protected:
    ->any var or method declared using "single leading underscore" inside a class
      considered as protected
    ->protected is meant for internal usage by child class
    ->it shud be used either in same class or its child classes and This is
      CONVENTION not an enforcement

3)Private:
    ->Any var or method declared using "double leading underscore" inside a class
      considered as private

    ->Private cannot be accessed directly from outside the class, it be accessed
      only from inside the class using methods

    ->used specially to hide sensitive data

Encapsulation:

->The process of protecting data by making the variable private and controlling
  their access through public setter and getter methods
or
  bundling/wrapping data and methods together and protecting data from outside access
->Direct access IS NOT given to sensitive data, BUT the class shud control How
  the data is read/modified
  
Steps to achieve Encapsulation:
1)A class should be public non abstract class
2)define  private variables
3)Have public setter method(to update the data with validation logic
4)Have public getter method(to access / read data safely

Note:
Setter method:
    -used to modify private data
    -usually expected to take 1 Paramete
    -validation logiv should be present inside it
    -not supposed to return any value

getter method:
    -used to access private data
    -usually does not take parameter
    -supposed to return any value


    Syntax:
        class ClassName:
            def __init__(self):
                self.__var=None #privateIV

            def set_var(self,newvalue): # Publicsettermethod to modify private
                #validation logic                variable upon validation
                self.__var=newvalue

            def get_var(self):  #publicgettermethod to read/Access private variable
                return self.__var
        obj=ClassName()
        obj.set_var(newvalue) #calling settermethod
        print(obj.get_var())  #calling gettermethod

Achieving Encapsulation using @Property decorator property decorator in python is
a way to access methods like variables

-There are 2 Decorators
    1)@property
    2)@<property>.setter

        1)Is a decorator, allows method to behave like "getter"
            ->instead of calling it normally like a method, we can ACCESS it like
              a normal attribute
              ex:
                  print(instanceref.variable)

        2)Is a decorator defines the "setter" for the same property
            ->allows you to ASSIGN a value like a variable, but indirectly it calls
              a method
              ex:
                  instanceref.variable=newvalue

Syntax:

class ClassName:
    def __init__(self):
        self.__var=None #private IV

    @property
    def var(self): #getter method
        return self.__var #access private IV inside class
    @var.setter
    def var(self,new_value): #setter method
        #validation Logic
        self.__var=new_value #access private IV inside class

obj=ClassName()
print(obj.var) #getter method gets calles if u access it like a variable
obj.var=value #setter method gets called if u access it like a variable

1)Getter MUST come first (becoz getter defines the property
2)Setter MUST come after the Getter (setter works on that property)
3)Always use same method name for both setter and getter and the property


Advantages of using Property:
1)it gives you attribute access with method control
2)looks like attributes but works like a method.
3)when requirements change, the code does not break
      
==================================================================================
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
    
