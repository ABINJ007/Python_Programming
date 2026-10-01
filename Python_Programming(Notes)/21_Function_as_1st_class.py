'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++ +=
Function as 1st class citizen in python
    -In Python function are treated as objects and hence they can be alieased,
     they can be passed, they can be returned just like in or strings

    Function aliasing:
        -assigning one Function's reference to another variable name or
        -here we are providing a new name to an existing function

def eat():
    print("eating survival")

consume = eat #FunctionAlising
eat()
print("++++++++++++++")
consume()
print(eat)
print(consume)

Passing Function as a Argument/Higher Order
Functions:
    ->A higher order function is one that takes another function as an input
      parameter or returns another function
    ->the function that is passed as an argument is called as callback.



def checkout(payment_mode):
    print(payment_mode) 
def cash():
    print("cash payment")
def card_swipe():
    print("swipe card")

checkout(cash)
checkout(card_swipe)

print("____________________________________")

def conduct_exam(subject):#HOF
    subject(90)
def java_exam(time):        #Call Back
    print(f"java exam last for {time} mintues")
def python_exam(time):      #Call Back
    print(f"python exam last for {time} mintues")
conduct_exam(java_exam)
print("======================================")
conduct_exam(python_exam)

#Nested function:
    ->A function which is defined inside another function is called a nested
     function.

    Syntax:
        def outer_fun_name():
            def inner_fun_name():
                pass
            inner_fun_name()
        outer_fun_name()

    +++++++++++++++++++++++++++++++++++

    def outer():                   #outer function Declaration
                           |-------#outer Function Body
    --->def inner():    <---       #outer function Declaration
        --->#innerfunctionbody

        inner()                #inner function call
    outer()                    #outer function call

    ->The inner function is only accessible within / inside the outer function
      implementation, unless it is returned.
    ->We use nested functions whn one function helps another function, but we
      don't want it to be used outside.
    ->It is like a helper but private inside the main function.

def outer():                        #OFD
    print("Outer Function body")    #OFB
    def inner():                    #IFD
        print("Inner Function body")#IFB
    inner()                         #IFC
    inner()
    inner()
    inner()
outer()                             #OFC

Enclosing Variables:
    ->Any Variable defined inside the outer function and accessed inside the
      nested/inner function is called enclosing variable
    ->A variable becomes an enclosing/ nonlocal variable only if the nested
      function uses it.
    ->The inner function can access ther outer Function variables.
    ->If we try to modify the variable of ther outer function(Ennclosing)
      inside the inner function, we get UnBoundLocalError, therefore we use
      "nonlocal" Keyword inside the nested Function.

a=300
def outer():                        #OFD
    print("Outer Function body",a)    #OFB
    def inner():                    #IFD
        print("Inner Function body",a)#IFB
    inner()                         #IFC
outer()                             #OFC

a=300
def outer():                       #OFD
    b=400
    print("Outer Function body",a,b)    #OFB
    def inner():                  #IFD
        c=500
        global a
        a =300+400
        nonlocal b
        b=400+200
        print("Inner Function body",a,b,c)#IFB
    inner()                         #IFC
outer()

Define a function called counter and it has count as variable with 0 as value
define a nested function called increment inside counter function
when u call increment function, the variable shud get incremented by 1 and
updated

call the increament 2 times and print the count value



print("=====================================================")
def counter():
    count=0
    def increment():
        nonlocal count
        count+=1
    def decrement():
        nonlocal count
        count-=1
    increment()
    decrement()
    print(count)
counter()
'''