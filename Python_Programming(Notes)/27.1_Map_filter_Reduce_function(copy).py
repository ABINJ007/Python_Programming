'''#def check_even(n):          #Callback
#    return n%2==0

def segregate(fun,cal):     #HOF
    lst=[]
    for i in cal:
        if fun(i):
            lst.append(i)
    return lst

#l=[3,8,12,13,19,22]
#sprint(segregate(check_even,l))

print(segregate(lambda n:n%2==0,[3,8,12,13,19,22]))
#################################################################################
#################################################################################

2.Filter Function:
    -filter out elements from an iterable based on a condition.
    -returns a filter object(an iterator).
    -filters only those elements where the function returns True and adds it into filter
     object.
    -
    -SYNTAX:
        filter(function,iterable)
        -function->this function passed as an parameter must take 1 parameter and return
         True or False.
        -iterable->sequence.

    example:
        print(list(filter(lambda n:n%2==0,[3,5,12,13,19,22])))
----------------------------------------------------------------------------------------
    2.
        l=["lathik","YASHAS","Sagar","Raj","SAI","Abin"]
        i want a list of manes which are having all leter that are capital
        
        l=["lathik","YASHAS","Sagar","Raj","SAI","Abin"]
        print(list(filter(lambda n:n.isupper(),l)))

-----------------------------------------------------------------------------------
    3.
        i want a list of counterfletters for each word in the list
        l=["lathik","YASHAS","Sagar","RAJ","SAI","Abin"]
        print(list(map(lambda i:len(i),l)))


#####################################################################################3
##################################################################################3##
3.reduce function:
    -its a function from functools module(from functools import reduce).
    -it applies a function "cumulatively" to the items of an iterable, reducing
     them to a single value.

     _SYNTAX:
         from functools import reduce
         reduce(function,iterable)

         function->a function that takes two arguments and shud return a sunglevalue
         -takes two arguments
         -returns one value

        1.
            def add(a,b):
                return a+b

            def compress(fun,col):
                res=0
                for i in col:
                    #res=res+i
                    res=fun(res,i)
                return res
                    
            l=[10,20,30,40,50]
            print(compress(add,l))

              OR

        

            from functools import reduce
            print(reduce(lambda a,b:a+b,[10,20,30,40,50]))

    -----------------------------------------------------------------------
            
        2.
            from functools import reduce
            l=[10,15,20,25,30,35]

            n1=filter(lambda i:i%2==0,l)
            print(list(map(lambda i:i**2,n1)))

                    #OR
            print(list(map(lambda i:i**2,filter(lambda i:i%2==0,l))))

'''

















