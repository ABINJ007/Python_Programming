'''
Iterator:
---------
An iterator in python is an object that allows you to traverse(iterate) through all elements of a collection, one element at a time, without needing to know how the collection is structured.
    ->it is Unidirectional(iterates from left to right)
    ->it supports partial iteration.

2)predefined function with respect to Iterator are
    1)iter(iterable) -
        -takes an iterable(list, tuble, string...) and returns an iterator object.
        -The iterator object keeps a cursor(internal pointer) that moves to the next element every time next() is called
    2)next(iteratorobject) -
        -returns the next element from thr iterator and advances the cursor.
        -when no elements are leftr, it raises StopIteration.

    NOTE: Iterator is EXHAUSTIBLE(single use object)
    - for loop internally uses iterator logic

l=[10,20,30,40]#iterable
itr_obj=iter(l)    #1)calling iter() that returns iterable obj
print(itr_obj)
#next(itr_obj))#10---------------------

#obj = next(itr_obj)#20--------->1
#print(obj)

#print(next(itr_obj))#

#for i in range(0,4):#
    #print("Money Multiplication")#
#
#print(next(itr_obj))#
#
#print(next(itr_obj))#-----------------------
#for i in itr_obj:------------------>2
#    print(i)
#print(tuple(itr_obj))-------------------3

#for loop internally makes use of iteratir and next function
i=0
while i<len(l):
    print(next(itr_obj))
    i=i+1
'''
