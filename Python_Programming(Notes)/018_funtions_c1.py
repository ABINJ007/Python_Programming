'''Functions
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
        
def-
    -is keyword  in python used to define a function
functionname-refers/label pointing to fucntion declaration acting as
placeholder to receive value

return-
    -it is a keyword in python
    -it returns a value(or multiple value) from the funtion to the caller/
    -it immediatly stops the funtions execution.
    -it transfers control back to the point where the funtion was called.
    -ant code after "return" is never excecution.

funtoional-
    -used to exceute a funtion.
    -arg1,arg2-> actual value that we pass when we call the funtion within the
     parenthod


def display():          #funtion declaration
    print("thrusday")   #funtion body

display()               #funtion call


def view():
    print("hah")

view()
view()


#######################################################################
#######################################################################

WORKING OF THE FUNTION:
    -funtion creation phase:
        -when python encounters a def keyword, it creates a funtion object
         in memory.
        -the funtions code is stored inside that object.
        -the funtions name becomes a reference pointing to that funtion object.
        -printing the funtion name(without the parathesis) displyas its memory
        refernce.

    -FUNTION EXECUTION PHASE:
        -when you call the funtion using parathesis, control is transfered to
         funtions code.
        -a new stack frame is created to hold its local variables(a,b and c).
        -after executing the code( or hitting return),
            -control goes back tot he caling point,
            -local variables are destroyed(stack frame gets destroyed).
            -but the funtion object itself remians in memory and can be
             called again.

    def display():
        print("th")

##############################################################################
##############################################################################
    -4 ways to defign funtion
    1.funtion without para and without return.
    2.funtion without para and wwith return.
    3.funtion with para and without return.
    4.funtion with para and with return.
    

#1.funtion without para and without return.
def display():
        print("th")

============================================================================
============================================================================

#2.funtion without para and wwith return.
    -syntax
    def funtionname():
        any code
        return value/s #value/s optional

     var=funtionname()
     print(var)
       
     

#create a funtion called wish_bday, and when we call this funtion it should
#return cake flavour

def wish_bday():
    print("happy birthday")
    return "chocolate"
print(wish_bday())
--------------------------------

#create a funtion called send_otp, and when we call this funtion it should
#return 3 digit number
def send_otp():
    print("otp")
    return "123"
print(send_otp())

==============================================================================
==============================================================================
#3.funtion with para and without return.
     syntax:
         def funtionaname(para1,para2...):
             #code

def add(a,b):
    print(a+b)
add(1,2)

#create a funtion called order_food which takes 3 para:name,dish,price.
#when you call this funtio, it output should be {name} is order {dish}
#which cost {price}

def order_food(name,dish,price):
    print(f'{name} has ordered {dish} which cost {price}')
    return
order_food("daniel","cake",100)

def book_ticket(name,tic_price):
    print(f'{name} has booked the ticket for rupees {tic_price}')
    return
book_ticket("daniel",100)
=============================================================================
=============================================================================
#4.funtion with para and with return.

    syntax:
         def funtionaname(para1,para2...):
             #code
             return value

#create a funtions.
#1st funtion is add, takes 2 para and when called it should return sum of them.
#

def add(a,b):
    return a+b

def sub(c,d):
    return c-d

def mult(e,f):
    return e*f

def divide(g,h):
    return g/h

print(add(1,2))
print(sub(2,1))
print(mult(1,2))
print(divide(6,2))
##########################################################################
##########################################################################

'''































     
