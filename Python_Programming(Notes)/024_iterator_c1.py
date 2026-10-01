'''
#ITERATOR:
    -it in python is an object that allows you to traverse(iterate) through
     all elements of a collection, one element at a time, without
     needing to know how the collection is structured.
    -it is Unidirectional(iterates from left to right)
    -it supports partial iteration.

    2.predefined function with respect to iterator are
    -1.iter(iterable):
        -takes an iterable (list,tuple,string,...) and returns an iterator obj.
        -the iterator object keeps a curor(internl pointer) that moves to the
         next element every time next() is called

    -2.next(iteratorobject)
        -returns the next element from the iterator and
         advances the cursor.
        -when no elements are left, it raises stopiteration.
        -using next() -> exhausted.

        Note: Iterator is exhausted (single use object)
        -for loop internally uses iterator logic.


        EXAMPLE:
        1.
            l=[10,20,30,40]    #iterable
            itr_obj=iter(l) #1. calling inter() that returns iterable obj
            print(itr_obj)  #when printing address
            a=next(itr_obj)   #next(iterableobject)
            print(a)             #output : 10
            print(next(itr_obj)) #output : 20
            print(next(itr_obj)) #output : 30
            print(next(itr_obj)) #output : 40

                            OR
                            
        2.
            l=[10,20,30,40]    #iterable
            itr_obj=iter(l) #1. calling inter() that returns iterable obj
            print(itr_obj)  #when printing address
            for i in itr_obj: #using for loop -> exhaut it.
                print(i)

        3.#using explicit typecasting->exaust it
            l=[10,20,30,40]    #iterable
            itr_obj=iter(l) #1. calling inter() that returns iterable obj
            print(itr_obj)  #when printing address
            print(tuple(itr_obj))  #output: (10, 20, 30, 40)

        4.
            l=[10,20,30,40]    #iterable
            itr_obj=iter(l) #1. calling inter() that returns iterable obj
            print(itr_obj)  #when printing address
            i=0
            while i<len(l):
                print(next(itr_obj))
                i=i+1
                        


                    

            '''
# generator
