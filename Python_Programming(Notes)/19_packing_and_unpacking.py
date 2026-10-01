'''
Packing:
    grouping / assigning multiple values into single variables.

    1.Manual packing->user decides which collection type and manuallly
     used brackets to pack the values




     2.Impicit.automatic packing
     -user does not decides explicitly the collection type.
     -python automatically collects multiple values into a tuple when no container
      specified


#implicit packing:
a=10,20,30,     #multiple values assigned into single variable default into tuple
print(type(a))


a="india","nepal","korea"
print(a[2])

##################################################################################
##################################################################################

UNPACKING:
    -extracting the values from a sequence(list,tuple,set,dict,str) and assigning them to
     individual valiables

    -Syntax:
        -var1,var2,var3,.,..=collection

    example:
        a=[10,20,30]
        a,b,c=a
        print(a)
        print(b)
        print(c)

    #tuple:
        a=(10,20,30)
        a,b,c=a
        print(a)
        print(b)
        print(c)

    #dict:
        a={1:10,2:20,3:30}
        a,b,c=a.values()
        print(a)
        print(b)
        print(c)

    #dict.items:
        a={1:10,2:20,3:30}
        a,b,c=a.items()
        print(a)
        print(b)
        print(c)

    #set:
        a={1,2,3}
        a,b,c=a
        print(a)
        print(b)
        print(c)

    #string:
        a="india"
        a,b,c,e,f=a
        print(a)
        print(b)
        print(c)
        print(e)
        print(f)

Note:
    -the number of variables should match the number of values you are trying to unpack from'
    the sequence.

==================================================================================
#extended Iterable Unpacking:
    when we do not know how many vakues to unpack.
    ->use *variablename, where the variablename will collect the remaining values into a LIST.

    -Syntax:
        var1,*var2=collection.

        example:
        1.
            l=[10,20,30,40,50,60]
            a,*b=l
            print(a) #10
            print(b) #[20,30,40,50,60]
        2.
            l=[10,20,30,40,50,60]
            *a,b=l
            print(a) #[10,20,30,40,50]
            print(b) #60

        3.
            l=[10,20,30,40,50,60]
            *a,b,c=l
            print(a)
            print(b)
            print(c)

    #NOTE:
        -only one *variable is allowed in unpacking assignment.
        -*variable can be at the beginning, or middle, or end.
        -the *variable always stores values in a LIST.
        -tuple,set,str(list of char)--everything in this datatype it is stored in list fromat
############################################################################
############################################################################
'''

















