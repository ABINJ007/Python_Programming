'''
Decorator
A Decorator is a function that modifies the behaviour of another function
without changing its code.
OR
A decorator is a function that:
    -takes another Function as input
    -adds extra behavior
    -returns a new function

    steps to define a decorator
    1)define a Nested function
    2)Outer Function shud take 1 parameter which accepts a function passed as
     argument
    3)Decorator Logic should be inside the inner Function
    4)the outer function shud return the inner Function Reference

    NOTE:
    1)The outerfunctionname usually can be named as decorator and innerfunctionname
      can be named as wrapper
    2)The no of parameters in the "function to be decorated" must be same with \
      the inner/wrapper function.
'''


def decorator(fun):  # Decoration function #HOF
    def wrapper():  # wrapper function containing the logic
        print("Take Gift paper")
        fun()
        print("Add a label on the gift")
    return wrapper


def gift():
    print("Coffee Mug Gift")


gift = decorator(gift)
gift()

'''
1) There is a function called cake which is to be decorated
2) I want to decorate this cake function with box,place candles and label it.
3) print statements BUt without modifying the original cake function
4)achieve this using decorator concept/logic.

def decorator(fun):#   <----------------Function alias
    def wrapper():              #|
        print("Take cakebox")   #|
        fun()                   #|
        print("add a label")    #|
    return wrapper              #|
def cake():#--------------------#|
    print("chocolate ")
cake = decorator(cake)
cake()

print("++++++++++++++++++++++++++++++++++")
def decorator(fun):
    def wrapper(name):#2
        print("Take Gift paper")
        fun(name)#3
        print("Add a label on the gift")
    return wrapper
def gift(name):#1
    print(f"{name} Gift")
gift = decorator(gift)
gift("Smiling Buddha")#4
#pass two parameters
print("++++++++++++++++++++++++++++++++++")
def decorator(fun):
    def wrapper(name, cost):#2
        print("Take Gift paper")
        fun(name, cost)#3
        print("Add a label on the gift")
    return wrapper
def gift(name,cost):#1
    print(f"{name} Gift cost {cost}")
gift = decorator(gift)
gift("Smiling Buddha",800)#4

#variable positional arguments
print("++++++++++++++++++++++++++++++++++")
def decorator(fun):
    def wrapper(*args):#2
        print("Take Gift paper")
        fun(*args)#3
        print("Add a label on the gift")
    return wrapper
def gift(*args):#1
    print("Gift selcted",args)
gift = decorator(gift)
gift("Smiling Buddha",700 ,"Prakashgiftstore", "ceramic", "gold","Mumbai")#4

print("++++++++++++++++++++++++++++++++++")
def decorator(fun):
    def wrapper(*args,**kwargs):#2
        print("Take Gift paper")
        fun(*args,**kwargs)#3
        print("Add a label on the gift")
    return wrapper
def gift(*args,**kwargs):#1
    print("Gift selcted",args,kwargs)
gift = decorator(gift)
gift("Smiling Buddha",700 ,"Prakashgiftstore",material="ceramic",Color="gold")#4

#Automatic decorator
print("++++++++++++++++++++++++++++++++++")
def decorator(fun):
    def wrapper(*args,**kwargs):#2
        print("Take Gift paper")
        fun(*args,**kwargs)#3
        print("Add a label on the gift")
    return wrapper
@decorator #AD
def gift(*args,**kwargs):#1
    print("Gift selcted",args,kwargs)
#gift = decorator(gift)
gift("Smiling Buddha",700 ,"Prakashgiftstore",material="ceramic",Color="gold")#4


#automatic decorator -> using "@decorator"
def decorator(fun): #decorator function #HOF  #function aliasing
    def wrapper(): #2 #wrapper having decoration logic
        print("function started")
        fun()   #3       #cake()
        print("function ended")
    return wrapper

@decorator
def login():#1   #original function to be decorated  #callback
    print("login operation")
    
@decorator
def payment():
    print("payment_operation")
    
@decorator
def logout():
    print("logout operation")
    
login()
payment()
logout()
'''