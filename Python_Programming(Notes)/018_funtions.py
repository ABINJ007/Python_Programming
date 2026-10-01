'''
Functions
    A function is a Named reusable block of code that performs a specific task.
Types:
    1)Predefined functions:
        -These are already defined by python to perform a specific functionlity
        ex: print(), input(), id(), len()
    2)UserDefined functions:
        These are functions that are created by the programmer to perform userspecific tasks/functionlities.
    Syntax:
        # function declaration  [1]
        def functionname(para1, para2, para3......):
            # Function block/body                                        [2]
            return values
        functionname(arg1, arg2, arg3, .....)  # functioncall/invocation  [3]

def - is keyword in python used to define a function
functionname-refers/label pointing to fucntion declaration acting as placeholder to receive value
return -
    -it is a keyword in python
    - it returns a value ( or multiple values ) from the function to the caller.
    -It immediately stops the function's Execution.
    -It transfer Control back to the point wher the function was called.
    -Any code after "return" is never executed.
fucntioncall -used to execute a function.
arg1,arg2 -> Actual value that we pass when we call the function within the parenthesis.
'''
print("_________________________________")
def display():       #Function Declaration
    print("Thursday")#Function Body
display()            #Function Call
display()
display()

def view():
    print("helloistme")
view()
view()
view()
'''
Working of a Function:
---------------------
    Function Creation Phase
        -when python encounters a 'def' keyword, it creates a function object in
         memory.
        -the Function's code is store inside that object.
        -The function word becomes a reference variable to that function object.
        -Printing the function name(without paratheses) displays its memory
         Reference.
    Function Execution Phase+
        -when you call the function using paratheses, control is transferred to
         the Fucntion's code.
        -A new stack frame is created to hold its local variables (a, b ..etc)
        -After Executing the code (or hitting "return"),
            -Control goes back to the calling point,
            -Local variables are distroyed,
            -But Function object itself remain in memory and can be called again.
------------------------------------------------------


def display():       #Function Declaration
    print("Thursday")#Function Body
display()            #Function Call
display()
display()
print(display)  #Address of display function


  #Whenever a function is called a stack frame will be created and Distroyed.

4ways of Defining Function:
    1)Function without para and without return
    2)Function without para and with return
    3)Function with Para and without return
    4)Function with parameter and with return


1)Function without para and without return
    def display():       #Function Declaration
        print("Thursday")#Function Body
    display()            #Function Call   
2)Function without para and with return:
    def functionname():
        #

        return value
        functionname()
            or
        var = Functionname()
        print(var)

#create a Function called wish_birthday and dwhen u call this function , it should return cake flavour.
def wish_birthday():        #FD
    print("Happy Birthday") #FB
    return "Chocolate"      #FB
wish_birthday()             #FC
print(wish_birthday())
#plate = wish_birthday()
#print(plate)


print("_______________________________")
import random
#create a Function called send_otp and dwhen u call this function , it should return 3digit number.
def send_otp():
    print("Successfully Entered")
    return random.randint(100,999)
print(send_otp())


def order_food(name, dish, price):
    print("{} has ordered {} which costs {}".format(name,dish,price))

order_food("cherian","icecream","1200")
    
def book_ticket(name,ticketprice):
    print("{} has booked a ticket price of {}".format(name,ticketprice))

book_ticket("cherian","1200")


#create 4 functions

def addition(num1,num2):
    value = num1+num2
    return value
print(addition(1,8))
def subtract(num1,num2):
    value = num1-num2
    return value
print(subtract(1,8))
def Multiply(num1,num2):
    value = num1*num2
    return value
print(Multiply(1,8))
def Divide(num1,num2):
    value = num1/num2
    return value
print(Divide(8,2))

3)Function with Para and without return
4)Function with parameter and with return
'''