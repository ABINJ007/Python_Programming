'''
Function as 1st class citizen in python

    -in python function are treated as object and hence they can be alased,
     they can be returned just like in or strings.

    #FUnction Aliasing:
    -assigning one functions reference to another variable name or
    -here we are providing a new name to an existing function.

    example:
   3.def eat():
        print("Eating is survival mechanism")

    print(eat)

    column=eat
    eat()

   2.def eat():
        print("Eating is survival mechanism")

    print(eat)
    column=eat
    eat()
    column()
    intake=eat
    intake()

    #Passing Function as a arguments/higher order Function:
        -higher order function is one that takes another function as an input parameter or
         returns another function.
        -the function that is passes as an arguments is called as Callback

        def checkout(paymentmode):
            print(paymentmode)

        def cash():
            print("cash.payment")

        def card_swipe():
            print("swipe")

        checkout(cash)
        checkout(card_swipe)

    3.
        def conduct_exam(subject):
            subject(90)

        def java_exam(time):
            print(f"java for {time}")

        def python_exam(time):
            print(f"python for {time}")

        conduct_exam(java_exam)
        conduct_exam(python_exam)

--------------------------------------------------------------------------------------------
Nested function
    -a function which is defined inside another function is called a nested function.

    Syntax:
    def outer_fun_name():           #outer function declaration
        def inner_fun_name():       #inner function declaration
            #inner function body    
        inner_fun_name()            #inner function call
    outer_fun_name()                #outer function call

    -the inner function is only accessible within/inside the order function implementation,
     unless it is returned.
    -we use nested functions when one function helps another function, but we dont want it to
    be used outside.
    -it is like a helper but private inside the main function.


    example:
    1.
        def outer():                             #OFD
            print("outer fun bloc")              #OFB
            def inner():                         #IFD
                print("inner function body")     #IFB
            inner()                              #IFC
        outer()

-----------------------------------------------------------------------------------
====================================================================================
Enclosing variables:
    -any variable defined inside the outer function and accessed inside the nested/inner
     function is called enclosing variable.
    -a variable becomes an enclosing/nonlocal variable only if the nested function uses it.
    -the innner function can access the outer function variables.
    -of we try to odify the variable of the outer function(enclosing) inside the innner
     function, we get unboundedlocalerror, therefore we use "nonlocal" keyword inside the
     nested function


    a=100  #GV1
    def outer():                             #OFD
        print("outer fun bloc",a)              #OFB
        def inner():                         #IFD
            print("inner function body",a)     #IFB
        inner()                              #IFC
                                      #OFC
    outer()


    2.
        a=100  #GV1
        def outer(): #OFD
            b=200    #local to user function
            print("outer fun bloc",a,b)              #OFB
            def inner():                             #IFD
                nonlocal b
                b=b+20                               #LV
                print("inner function body",a,b)   #IFB
            inner()                                  #IFC
                                                     #OFC
        outer()


    3.
        a=100  #GV1
        def outer(): #OFD
            b=200    #local to user function         #OFB
            c=300
            def inner():                             #IFD
                nonlocal b,c
                global a
                b=b+20                               #LV
                c=c-50
                a=a*2
                print("inner function body",a,b,c)   #IFB
            inner()                                  #IFC
                                                     #OFC
        outer()




a=100  #GV1
def outer(): #OFD
    b=200    #local to user function         #OFB
    c=300
    def inner():                             #IFD
        nonlocal b,c
        global a
        b=b+20                               #LV
        c=c-50
        a=a*2
        print("inner function body",a,b,c)   #IFB
    inner()                                  #IFC
                                             #OFC
outer()


define a function called counter and it has count as variable with 0 as value.
define a nested function called increament inside counter function.
when u call increament function, the count variable shud get increamented by 1 and updated

call the increament 2 times and print the count value.

def counter(count=0):
    def increament():
        nonlocal count
        count=count+1
        print(count)

    def decrement():
        nonlocal count
        count=count-1
        print(count)
        
    increament()
    decrement()
    

counter()





Clousure
#closure is an inner function that remenbers and can access the variable from its enclosing
 (outer) function, even after the outer function has finished executing.

-steps needed to create a closure
1.create a outer function with a variable local to that puter function.
2.define an inner function that uses that outer variable(i.e,enclosing variable)
3.outer function RETURNS the inner function and this activates the closure.
NOTE: even though the outer function finishes its axecution, the
 outer function variable will be still remembered by inner function.
 

============================================================================
===========================================================================

def outer():
    print("Outer function boody")
    a=100
    def inner():
        print("inner function body",a)
    return inner

inner=outer()
inner()
inner()
inner()

#################
###-define an outerfunction called as get_color which contains enclosing variable called as
    color having red as the value.
   -define a nested function called show_color and showcase closure concept


   

def get_color():
    color="red"
    def show_color():
        print(color)
    return show_color

sol=get_color()
sol()

##########################################################

# -define an outerfunction called as counter which contains enclosing variable called as
    count having 0 as the value.
   -define a nested function called increament and showcase closure concept



def counter(count=0):
    def increament():
        nonlocal count
        count=count+1
        print(count)
    return increament

icr=counter()
icr()
icr()
icr()
################################################################################
################################################################################


Decorator:
'''
    
        
