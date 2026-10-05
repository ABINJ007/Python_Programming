'''
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
Contructor/Initialiser ->
    -It is a block of code / special dunder method used to declare and
      initialize instance variables of an instance
    -Syntax:
        class ClassName:
            def __init__(self):  # <-Initializer/constructor gets executed every
                                time an instance is created
                # Initialisation

        objref = ClassName()
        -the constructor/Initializer must be written within the class and its name should be __init__(self)
        -self must be the 1st implicit parameter in the constructor and it refers to the current invoking instance
        -using self parameter inside the constructor, we create and initialise instance variables using syntax
                ->self.variablename = value

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
            ->This method works on class level data and not on instance
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
    ->it receives the current instance reference as the 1st parameter referred
      to self
    Syntax:
        class ClassName:
            def method_name(self,para1,para2,......):
                #method body/logic
        reference=ClassName()
        reference.method_name(arg1,args,...)

    ->if there are "n" parameters in the instance method, we shud pass "n-1"
     arguments during the instance method calling
      
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
'''
