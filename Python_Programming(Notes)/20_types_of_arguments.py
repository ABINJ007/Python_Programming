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
4)
->A Default argument is a parameter in a function declaration which already has a predefined value/default value.
->If the function caller does not provide a value for that parameter, the default value will be used.
->But if we pass a value for the parameter, the new value
 will replace the default value.          

   

def display(age=0,height=0.0,ismarried=False):
    print(age)
    print(height)
    print(ismarried)

display(43)

Order of Passing all arguments:
1)positional args / required args
2)*args / variable positional args
3)Default args (function declaration ) , keyword args(function call)
4)**kwargs(variable keyword argument.

Types of variables based on functionscope:
    Global variable
    local variable

1)Global variable
    ->Variable which is declared outside of all functions & classes.
    ->The variable which are created in main space/ stack.
    ->Global variable can be accessed from anywhere in the module
    ->Global variable can be modified outside the function, but to modify a
      global variable inside a function we need to use the global keyword, or
      else it will throw unboundlocal error.
    


a = 200 #GV

def fun():#FD
    global a #use global keyword when we are trying to modify GV inside the
    Function.
    a = a + 300#Modification of GV inside the function
    print("Function Body")
    print("accessing the GV inside the function",a)

print("accessing the GV outside the function",a)#accessing the global varibale
outside the Function
fun()#function call
a = a+50#Modification of GV outside the function
print(a)
fun()

print("-------------------------------------------")


a1 = 100 #GV
a2 = 300 #GV
def fun():#FD
    global a1, a2
    #global a1
    #global a2 #use global keyword when we are trying to modify GV inside the
    Function.
    a1 = a1+300#Modification of GV inside the function
    print(a1)
    print("Function Body")
    print("accessing the GV inside the function",a1)
    a2 = a2 * 5
    print("accessing the GV inside the function",a2)

print("accessing the GV outside the function",a)#accessing the global varibale
outside the Function
fun()#function call
a1 = a1+50#Modification of GV outside the function
print(a2)
fun()

2)Local Variable:
    ->It is a variable  which is declared inside the function
    ->It can be accessed only inside the function.
    ->Local varible can be modified inside that function only.
    ->Local variable are created inside the local variable scope of the function,
      and once the function execution is completed, they are destroyed.
NOTE:
->Parameters are local variable of that function.
----------------------------------------------------------
Note:
->when both global and local variables have the same name inside the function,
  Python uses the local varible first


def fun():
    b = 100 #LV
    print("Access Lv inside that Function", b)
    b = b + 5
    print("accessing modified value",b)
fun(100)
print("access LV outside that function")



print("_________________________________________________")
a=100 #GV1
def fun():
    a=200#LV1
    print(a)
fun()
print(a)
'''

