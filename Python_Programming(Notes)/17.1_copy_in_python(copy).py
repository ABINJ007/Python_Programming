'''
COPYING OF PYTHON:

    1.general copy:
        -assigning one variable to another.
        -both variables refer to the same object in memory.
        -changes made through one variable reflect in the other.
        


list1=[10,20,30,[40,50]]
list2=list1
list1[2]=200
print(list2)
list2[1]=300
print(list1)

import copy
list1=[10,20,30,[40,50]]
list2=copy.copy(list1)
print(list2)
list1[2]=200
print(list1)
print(list2)
list1[3][0]=500
print(list2)

############################################################################
###########################################################################


3)Deep Copy:
------------
    -Creates a new container object and Recursively copies all nested objects
     too.
    -Changes in one do not affect the other.

Functions
    A function is a Named reusable block of code that performs a specific task.
Types:
    1)Predefined functions:
        -These are already defined by python to perform a specific functionlity
        ex:print(),input(),id(),len()
    2)UserDefined functions:
        These are functions that are created by the programmer to perform
        userspecific tasks/functionlities.
    Syntax:
        def functionname(para1,para2,para3.,....): #function declaration  [1]
            #Function block/body                                        [2]
            return values
        functionname(arg1,arg2,arg3,.....)  #functioncall/invocation  [3]
        
def-is keyword  in python used to define a function
functionname-refers/label pointing to fucntion declaration acting as
placeholder to receive value
return-
    -it is a keyword in python
    -it returns a vlue
        


'''












