'''
for i in range(1, 11):
    print("hello")

Looping = repeating a set of instructions multiple times until a condition is
          satisfied
     ->ALSO used to traverse Elements from collection

why to use loops:
    -Reduce code duplication (don't repeat same lines again and again)
    -Automate repetitive tasks (e.g., check 1000 files, send 1000 emails ,
     print 1000 numbers).
    -Work with collections(strings, lists, dicts ,etc).

Three Types of loops:
        -For Loop
        -While Loop
        -Nested For Loop
-----------------------------------------------------

For Loop:-->Known iterations
        -Best when you know in advance how many times to loop.
        -works with range() annd collections (list, tuple, string, dict).
        For loop Syntax:

            For varible in Sequence:
                #loop body(code to repeat)

        -variable -> takes on value from the sequence , at a time.
        -Sequence ->can be a range, list, tuple, string, or any iterable.
        -loop body->for each item or each value taken from the sequence, the
         indented for loop block runs
    
        


t = (1, 2, 3, 4, 5, 6, 7)
for i in t:
    print("Wednesday")

print("----------------------")

for i in range(1,51):
    print("Wednesday",i)

#print me numbers 4,8,12,16,20,24,28 uding for loop

for i in range(4,29,4):
    print(i)

    print("----------------------------------")

#l = [10, 20, 30 , 40 , 50, 60 , 70]
#for i in range(0,len(l),3):
 #s   print(l[i])

l = [10, 20, 30 , 40 , 50, 60 , 70]
for i in range(5,0,-2):
    print(l[i])
    
s={11,22,33,44}
#with for loop

d={1:10, 2:20, 3:30}
#for loop

st = "Aizen"
#for loop

for i in s:
    print(i)
for i in d.items():#bydefault when dict is used with for, we getkeys
    print(i)
for i in st:
    print(i,sep="\n",end="    ")


#when going thru each keys using for loop, if key matchs "yagami" print its value
d={"goku":"DragonBallz","yagami":"DeathNote","ichigo":"Bleach","migi":"parasyte"}


#for i in d:
 #   if i == "yagami":
  #      print(d.get(i))

for j in d:
    if "i" in j:
        print(d[j].upper())

2)while loop --> Unknown iterations
-Best when you don't know how many times you need to loop.
-Runs until condition becomes False.

while loop Syntax:
    Initialisation
    while Condition:
          -------------------
    ---->| #while loop block |
         |                   |
         | updation Logic    |
          -------------------
-condition --> Boolean expression (True/False)
-Loop runs as long as conditon is True

count = 80
while count>61:
    print(count)
    count = count  -3
l = [90, 80, 70, 60, 50, 40, 30, 20, 10]
i = 0
while i < 7 :
    print(l[i])
    i = i - 2
Loop control statements:
-----------------------
    1)break
    2)continue
    3)pass

            -how we can extra control or interruption during loop execution.
        
1)break ->it is a keyword in python.
        ->Stop the loop immediately and exits from the loop completely. Any statements inside the loop after "break" won't run.
        ->After that, the program continues after the foor /while loop block ie) remaining code outside for/while loop normally executes
        ->By doing this , it saves time by avoiding unnecessary looping execution

        Syntax of "break" in Loops:
        for variable in sequence
                if condition:
                    break  #exits the loop completely
                #rest of code
        while condition:
            id condition_to_stop:
                break      #exits the loop completely
                #rest of code

print("startS")
for i in range(45,68,1):
    if i%11 == 0:
        print(i)
        break
    
print("end")

print("______________________________________________________")

rolls=[497,19390,32,18,7,38,24]

for i in rolls:
    if i == 18:
        print(f"found:{i}")
        break

2)Continue -> it is a keyword in python
           -> Skip current iteration, Move to next iteration.
           -> It Doesn't stop the loop, only Skips that current iteration
           -> It will skip the remaining lines below the continue, insiderr the loop and jumps to the newxt cycle of the loop.
           -> continue helps ignore unwanted cases.

           Syntax:
               for variable in sequence:
               ----->if condition_to_continue:
                     ------>Continue

                     #Remaining Lines below  the continue inside loop will skip only if continue is Encounted.

for i in range(43,63):
    if i%2 == 0 and i%5==0:
        continue
    print(i)
    
print("_____________________________________________")
marks = [45, -74, 62, 74, 52, -48, 92, -35, 27, 93]
for i in marks:
    if i<0:
        continue
    print(i)


3)pass -> Do nothing(placeholder)
    -it is a keyword in python
    -Does literally nothing when executed.
    -Used as a placeholder when you haven't written the code yet.
    Syntax:
        for i in sequence:
            pass
        while condition:
            pass
   
if 5<6:
    pass
for i in range(3,6):
    pass
i=7
while i<9:
    pass
#instead of having empty block of code, use pass keyword in its place.
     
Nested For Loop:
---------------
    -One For loop inside another for loop.
    -when outer loops runs once, The inner loop runs fully every time.
    -used when you want all combinations from two groups.
    Syntax:
        for variable in sequence1:
        ----->for variable2 in sequence2:  <-----outer for block
        --------->inner for loop Block
        


for i in range(2,5,1):
    for j in range(1,4,1):
        print(f'{i} * {j} = {i*j}')

M=["dosa","idle","puri"]
S=["chutney","sambar","aloocurry"]
for Ms in M:
    for Ss in S:
        print(f"{Ms} {Ss}")

For Else Block:
---------------
    -When you're looping, you often want to do something if the loop completed Normally (no break keyword id encountered.
    -If the loop was interrupted with break keyword, then else break block will Not be executed.
    Syntax:
        for variable in sequence:
            for loop block:
        else:
            #else block will run once at the last, when the above loop completes nnormally without executing break.
    -The else block runs only if loop completes normally(no break)
    -If the loop was
    

Rollno = [77,72,7,73,79,72,71]
Rol = int(input("Enter RollNO:"))
for R in Rollno:
    if R == Rol:
        print("Found")
        
else:
    print("not")


Nested Collection:
    A nested Collection means a collection (list, tuple, set, or dict) that contains another collection inside it.

    1)Nested List
    2)Nested Dict
    3)List of Dictionary
    JSON Stands for JavaScript Oject Notation
    It's basically a format to store and share structured data especially b/w client and server in web apps, APIs, etc.
    4)Dictionary of List(list inside dictionary) used in API or in dataframe in Pandas

    NEsted list:
        Having or placing  multiple list inside another list is known as Nested list

l = [["Amy", 23, 94000],["Ben", 44, 75000],["Chad", 12, 80000]]
for i in l:
    if i[2]>90000:
        print(i[0].upper())
        i[0] = i[0].upper()
        print(l)

Nested Dictionary:  
----------------

company={'emp1':{'name':'Amy','salary':94000,'dept':'hr'},
         'emp2':{'name':'Ben','salary':75000,'dept':'Research'},
         'emp3':{'name':'Chad','salary':80000,'dept':'Sales'}
         }
print(company)
print("_______________________________________________")
for i in company.values():
    #if i["dept"] == "HR" or i["dept"] == "hr":
    #if i["dept"].upper() == "HR" :
    if i["dept"].lower() == "hr" :
        #print(company[i]['name'])
        
        #print(company.get(i).get("name"))
        print(i["name"])
        
for i in company.values():
    print(i['name']['


1)Nested List
2)Nested Dict
3)list of dictionary:
    JSON stands fro javaSript Object notation
    It's basically a format to store and share structured data-
    especially b/w client and server in web apps, APIs, etc.
4)DICTIONARY of LIST(list inside dictionary) used in API or in dataframe in pandas


company=[{'name':'Amy','salary':94000,'dept':'hr'},
         {'name':'Ben','salary':75000,'dept':'Research'},
         {'name':'Chad','salary':80000,'dept':'Sales'}
         ]
for i in company:
    print(i)

company={
    'names':["Amy","Ben","Chad"],
    'depts':["HR","Sales","Marketing"],
    'salaries':[94000,78000,84000],
    'ids':[101,113,124]
    }

#for i in company:
#    print(i)


for i in company['names']:
        print(i)

Copying in Python
1)General Copy
    -assigning one variable to another.
    -Both Variables refer to the same object in memory.
    -Changes made through one varible reflect in the other.

list1=[10,20,30,[40,50]]
list2=list1
list1[2]=200
print(list2)
list2[1]=300
print(list1)




2)Shallow Copy:
    -creates a new container object, but copies only the references of elements inside it (not the nested ones).
    -Changes in nested elements still affect both copies.
'''
import copy
list1=[10,20,30,[40,50]]
list2=copy.copy(list1)
list2[2]=600
print(list1)
print("___________________________________")
print(list2)
print("___________________________________")
list1[3][0]=500
print(list1)
print(list2)
'''
3)Deep Copy:
------------
    -Creates a new container object and Recursively copies all nested objects too.
    -Changes in one do not affect the other.

    

Functions
    A function is a Named reusable block of code that performs a specific task.
Types:
    1)Predefined functions:
        -These are already defined by python to perform a specific functionlity
        ex:print(),input(),id(),len()
    2)UserDefined functions:
        These are functions that are created by the programmer to perform userspecific tasks/functionlities.
    Syntax:
        def functionname(para1,para2,para3......): #function declaration  [1]
            #Function block/body                                        [2]
            return values
        functionname(arg1,arg2,arg3,.....)  #functioncall/invocation  [3]
        
def-is keyword  in python used to define a function
functionname-refers/label pointing to fucntion declaration acting as placeholder to receive value
return-
    -it is a keyword in python
    -it returns a value (or multiple values ) from the function to the caller.
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

Packing:
    Grouping / assigning multiple values into a single varible.

    1)manual packing -> user decides which collection type and manully uses brackets to pack the values














3)Variable length Arguments->
    Used in function whne you don't know how many aruments will be passed during function call.
    3.1)Variable positional arguments:
        *args -> variable positional arguments(used in function declaration)
        -We used *args in the function declaration which collects extra positional arguments into tuble
        -args* can be used only in the dunction declaration
        -args* must come after  positional arguments

        NOTE1=>when we *args in the "Function declaration", we can see packing.
        NOTE2=>when we

















        

print("----------------------------------")
def display(bio,maths,**kwargs):
    print(bio,maths,kwargs)
display(bio = 99,maths = 98,phy =97, soc = 89)
    

def display(bio,maths,phy,soc):
    print(bio,maths,phy,soc)
d={"bio": 99,"maths": 98,"phy": 97, "soc": 89}
display(**d)

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

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
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


Closure:
    A Closure is an inner function that remembers and can access the variables
    from its enclosing (outer) function, even after the outer function has
    finshed executing.

    steps needed to create a closure:
    1)Create an outer Function with a variable local to that outer function.
    2)Define an inner Function that uses that outer Variable
    3)Outer Function "Returns" the inner function and this activites the closure.
    NOTE:even though the outer functiion finishes its execution, the outer
    function's variables will be still remembered by inner function

    Usage:
    1)Used in Decorates
    2)Access Control
    3)cashing

