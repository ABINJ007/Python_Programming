'''
Inheritance:
------------
The process of 1 class acquiring the properties of another calss
    ->The class which shares the properties -> parent or super or base class
    ->The class which acquires the properties -> child or sub or derived class
    ->Inheritance can be referred to as 'IS -A -Relationship'
    ->In python we can inherit variables and methods

Types of Inheritance:

1)Single Level
2)Multi Level
3)Heirarchical Level
4)Multiple Level
5)Hybrid Inheritance

1)Single level
      - ----
      | A |
      -----
        ^
        |
        |
      -----
      | B |
      -----
Class A:  # parent class
    -> A states
      A Behaviours
Class B(A):  # child class
    -> B class states
    -> B class behaviours

1)single Level-.combination of 1 suberclass and 1 subclass

NOTE:
    MRO -> Method resolution Order
    -> It is a method order in which python searches classes to find that method
    -> This is releveant only when there is more tha 1 inheritance path
    -> ClassName.__mro__

2)Multi-Level -> Combination of 2 or more singlelevel inheritance in a sequential
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
'''