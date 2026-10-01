'''
Decorator:
    -it is a function that modifies the behaviur of another function without changing
    its code..
        

    OR

    a decorator is a function that:
    -takes another function as input.
    -adds extra behavour.
    -returns a new function.

    #Steps to define a decorator:
    -1.define a nested function.
    -2.outer function shud take 1 parameter which accepts a function passed
       as arguments.
    -3.decorator logic shud be inside the inner function
    -4.the outer function shud return the inner function refernce.

    #NOTE:
    -1.the outerfunctionname usually can be named as decorator and
       innerfunctionname can be named as wrapper.
    -2.the no of parameters in the function to be decorated a=must be same
       with the inner/wrapper function.

       Example"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           1.
            def decorator(fun):
                def wrapper():
                                print("select gift paper")
                    fun()
                    print("add label to the gift")

                return wrapper

           def gift():
               print("coffee mug gift")



           gift=decorator(gift)
               gift()

            #2.there is a function called cake which is to be decorated.
            #i want to decorate this cake function with box,place candle
            #and label it print statement but without modifying the original
            #cake function.
            #achieve this using decorator concept/logic.

            def decorator(fun):#decorator function #HOF  #function aliasing
                def wrapper():#wrapper having decoration logic
                    print("take the box")
                    fun()          #cake()
                    print("place candle and label")
                return wrapper

            def cake():   #original function to be decorated  #callback
                print("chocalate cake")
            cake=decorator(cake)
            cake()


            3.#with parameter->(name)
            def decorator(fun):#decorator function #HOF  #function aliasing
                def wrapper(name):#wrapper having decoration logic
                    print("take the box")
                    fun(name)          #gift()
                    print("place candle and label")
                return wrapper

            def gift(name):   #original function to be decorated  #callback
                print(f"{name} gift")
            gift=decorator(gift)
            gift("cake")

            4.
            def decorator(fun):#decorator function #HOF  #function aliasing
                def wrapper(name):#wrapper having decoration logic
                    print("take the box")
                    fun(name)          #cake()
                    print("place candle and label")
                return wrapper

            def cake(name):   #original function to be decorated  #callback
                print(f"{name} cake")
            cake=decorator(cake)
            cake("chocolate")

            5.
            #with two parameter(name,cost)
            def decorator(fun):#decorator function #HOF  #function aliasing
                def wrapper(name,cost):#wrapper having decoration logic
                    print("take the box")
                    fun(name,cost)          #cake()
                    print("place candle and label")
                return wrapper

            def cake(name,cost):   #original function to be decorated  #callback
                print(f"{name} cake of rupees {cost}")
            cake=decorator(cake)
            cake("chocolate",100)

            5.#*args
            #with two parameter(name,cost)
            def decorator(fun): #decorator function #HOF  #function aliasing
                def wrapper(*args): #2 #wrapper having decoration logic
                    print("take the box")
                    fun(*args)   #3       #cake()
                    print("place candle and label")
                return wrapper

            def cake(*args):#1   #original function to be decorated  #callback
                print(f"gift selected ",args)
            cake=decorator(cake)
            cake("chocolate",100,"gift store","ceramic","gold","mumbai") #4

            7.
            #with *args,**kwargs
            def decorator(fun): #decorator function #HOF  #function aliasing
                def wrapper(*args,**kwargs): #2 #wrapper having decoration logic
                    print("take cake box")
                    fun(*args,**kwargs)   #3       #cake()
                    print("add label")
                return wrapper

            def cake(*args,**kwargs):#1   #original function to be decorated  #callback
                print(f"selcake selected ",args,kwargs)
            cake=decorator(cake)
            cake("chocolate",100,"gift store",material="ceramic",color="gold") #4

            8.#automatic decorator -> using "@decorator"
            def decorator(fun): #decorator function #HOF  #function aliasing
                def wrapper(*args,**kwargs): #2 #wrapper having decoration logic
                    print("take cake box")
                    fun(*args,**kwargs)   #3       #cake()
                    print("add label")
                return wrapper

            @decorator  #above the original 
            def cake(*args,**kwargs):#1   #original function to be decorated  #callback
                print(f"selcake selected ",args,kwargs)
                
            cake("chocolate",100,"gift store",material="ceramic",color="gold") #4

'''


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



















