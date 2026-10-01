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
'''