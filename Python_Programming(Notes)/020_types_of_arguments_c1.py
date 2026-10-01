'''
TYPES OF ARGUMENTS write funtion:
    1.positional/sequenced args
    2.keyword args
    3.variable length arg
    4.default args

#1.positional/sequenced args:
    -values are passed in the same order as th parameters present in the funtion declaration.
    -order matters.
    -number of parameters = number of args.

    DISADVANTAGE:
    -dev need to remenber the order.

    example:
        def write(brand,colour):
        print(f"we are writing in {colour} pen of {brand}")

write("doms","blue")
---------------------------------------------------------------------------

#2.keyword args:
    -values are passsed using paramenter names during funtion call.
    -therefore, order does not matter. count matters.
    -this methods are used to overcome the positional args.
    -number of parameters = number of args.
    -cannot pass the same keyword arg twice.
    -positional arg should come before the keyword args.

    EXAMPLE:
        def write(brand,colour):
            print(f"we are writing in {colour} pen of {brand}")

        write(colour="blue",brand="doms")  #(colour is parameter name)

----------------------------------------------------------------------------

#3.variable length arg:
    -used in funtion declaration when you dont know how many arg will passed during funtion
     call.


     3.1).variable positional arg:
         -*arg->variable positional argts( used in funtion declaration)
         -we use *args in the funtion declaration which collects extra positional args into
          TUPLE.
         -*args can be used only once in the function declaration.
        
         -*args must come after positional args
         -NOTE:
             -when we use *args in the function declaration, we can see packing.
         -Note:
             -when we use *iterable  in the funtion call, we can use uppacking
               and it unpacks into positional args and make sure that the number
              
               
         -def funtoionname(*arg):  #FD
             print(args)           #FB
          funtion(v1,v2,v3,..)     #FC

          EXAMPLE:
        def dream_big(*args):
            print(args)

        dream_big("criket","docter","police","pilot","average","athlete")

        -exaple(unpacking using star iterable):
        def remove(a,b,c):
            print(a)

        l=[11,12,13]
        remove(*l)


        def remove(*args):
    print(args)

l=[11,12,13]
remove(*l)
----------------------------------------------------------------------------
#
        **kwargs -> variable keyword arg.
        -we use **kwargs in the function declaration which collects extra keywords arguments
        into dictionary.
        -**kwargs can be used only once
        -**kwargs must come last in the function decelaration.
        -it also collects keyword args which are not matched by any parameters
        NOTE1=>when we use **dictionary in the function call, we can use see unpacking and it
        unpacks into keywords args and make sure tht the keyname which is unpacked shud match
        the parameter name.
        NOTE=>when we use **kwargs in the funtion declaration, we can see packing


        example:
        1.  def display(**kwargs):
                print(kwargs)

            display(soc=88,phy=99,bio=39)

        2.
            def display(bio,soc,**kwargs):
                print(bio,soc,kwargs)

            display(soc=88,phy=99,bio=39,hin=24)

        3.
            def extract(phy,soc,mat,bio):#unpacking
                print(phy,soc,mat,bio)

            d={"phy":88,"soc":56,"mat":89,"bio":98}
            extract(**d)

---------------------------------------------------------------------------
#4.default args:
    -a default args is a parameter in a function declaration which already has a
     predefined value/default.
    -if the function caller does not provide a value for that parameter, the default value
     will be used.
    -but if we pass a value for the parameter, the new value will replace the default
     value.

    EXAMPLE:
    1.
        def display(age=0,height=00,ismarried=False):
            print(age)
            print(height)
            print(ismarried)

        display()
        display(3.2)
        display(34,58)
        display(88,8.8,True)

=====================================================================
=====================================================================
Order of passing all agns:
    1.positional args/reqiured args.
    2.*args/variable positional args.
    3.Default args(funtion declaration), keyword args(function call).
    4.**kwargs.



Types of variables based on funtionscope:
    -GLobal varable
    -Local variable

    1-Global variable:
        -variable which is declared outside of all funtions and classes.
        -the variable which are created in main space?stack.
        -glbal varaible can be modified outside the funtion, but modify a global variable
         inside a function we need to use the global keyword, or else iit will throw
         unboundlocalerror.


    Example:
    1.  a=100
        def fun():
            print("function body")
            print("accessing the GV inside the funtion",a)

        print("accessing the GV outside the function",a)
        fun()#function call


    2.
        a=100
        def fun():
            global a
            print("function body")
            print("accessing the GV inside the funtion",a)
            print(a+300)

        print("accessing the GV outside the function",a)
        fun()#function call


        a=a+50
        print(a)
--------------------------------------------------
    2-Local variable:
        -it is a variable which is declared inside the function.
        -it can be accesed only inside the function.
        -local variable can be modified inside that function only.
        -local variables are created inside the local variable scope of the function, and
         once the function execution is completed, they are destroped.

         NOTE:
         parameters  are local variables of that function.

         example:
         def fun():
            a=100
            print("access LV inside the function",a)

        fun()
         ---------------------------------------------------------------

         NOTE:
         when both global and local variables have the same name inside the function,
         python uses the local variable first


    
        
        
'''
a=100
def fun():
    a=200 
    print(a)
    

fun()

              









