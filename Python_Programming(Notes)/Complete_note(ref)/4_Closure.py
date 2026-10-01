def outer():
    print("outer function body")
    def inner():
        print("inner function body")
    return inner
outer()
'''
define an outerfunction called as get_colour which contains enclosing variable
called as colour having read as the value
define a nested Function called show_colour and showcase closure concept
'''
def get_colour():
    colour="red"
    def show_colour():
        print("colour")
    return show_colour
show_colour=get_colour()
show_colour()

def counter():
    count=0
    def increment():
        nonlocal count
        count+=1
        print(count)
        
    return increment
increment=counter()
increment()
increment()
increment()
increment()
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
def decorator(fun):#Decoration function #HOF
    def wrapper(): #wrapper function containing the logic
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



def decorator(fun):
    

Iterator:
---------
An iterator in python is an object that allows you to traverse (iterate) through all elements of a collection, one element at a time, without needing to know how the collection is structured.
    ->it is Unidirectional(iterates from left to right)
    ->it supports partial iteration.

2)predefined function with respect to Iterator are
    1)iter(iterable)-
        -takes an iterable (list, tuble, string...) and returns an iterator object.
        -The iterator object keeps a cursor (internal pointer) that moves to the next element every time next() is called
    2)next(iteratorobject)-
        -returns the next element from thr iterator and advances the cursor.
        -when no elements are leftr, it raises StopIteration.

    NOTE:Iterator is EXHAUSTIBLE (single use object)
    -for loop internally uses iterator logic
'''
l=[10,20,30,40]#iterable
itr_obj=iter(l)    #1)calling iter() that returns iterable obj
print(itr_obj)
#next(itr_obj))#10---------------------

#obj = next(itr_obj)#20--------->1
#print(obj)

#print(next(itr_obj))#

#for i in range(0,4):#
    #print("Money Multiplication")#
#
#print(next(itr_obj))#
#
#print(next(itr_obj))#-----------------------
#for i in itr_obj:------------------>2
#    print(i)
#print(tuple(itr_obj))-------------------3

#for loop internally makes use of iteratir and next function
i=0
while i<len(l):
    print(next(itr_obj))
    i=i+1
'''
Generator:
----------
-Generator is a Function that is used to create a custom sequence of elements using the "yield" keyword.
-If a user-defined function contains at least one yield keyword, then that function becomes a generator function.
-Generators generate values one-by-one (not all at once).
-Generators are 'mainly used to create custom sequence (like even numbers, odd numbers, fibanacci, primes, infinte sequences,large data streams).

-Generators object is created ONLY ONCE, When the "Function containing YIELD keyword" is called.
-Each yield returns ONE value, when next() or for loop asks for it.
yield:
    when python executes yield:
1.It returns the yielded value to the called.
2.It "pauses" the function (remembers variables and the next line).
3.When you call next() again, it "resumes right after yield".
4.Automatically creates an iterator.

'''
print("---------------------------------")
def fun():#generator Function
    yield 10
    yield 20
    yield 30

gen_obj = fun()  #when generator function is called, generator object is returned.
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print("---------------------------------")

def fun():
    value=0
    yield value

    value = value + 1
    yield value

    value = value + 2
    yield value**2

    value = value + 3
    yield value**3

    value = value - 2
    yield value**2



gen_obj=fun()

'''
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))

'''
for i in gen_obj:
    print(i)

    
'''
Lambda Function:
    A lambda Function is a small, anonymous function defined using the lambda keyword  
OR
    A labda Function us a function without a name, written in a single line, and used for short operations.
    NOTE:LAMBDA Function is best "when we need to pass simple helper function " for a higher order function (Function which takes other Function as a parameter)    
Syntax of Lambda:
lambda arguments : Expression

Key Rules
    -NO Function name
    -NO return keyword
    -expression result is returned automatically
    -Only ONE expression allowed



'''
print("______________________")
def add(a,b):
    return a + b

lambda a,b:a+b
print((lambda a,b:a+b)(10,30))
      
def square(n):
    return n**2

lambda n:n**2
print((lambda n :n**2)(10))

def check_even(n):
    return n%2==0

lambda n:n%2==0
print((lambda n:n%2==0)(20))
'''
Calling a Lambda Function:
    Approach 1 - Assign to variable
    Approach 2 - Direct call
        syntax:
            lambda (para1,para2,para3,.....:Expression)(arg1,arg2,arg3,...)
                    -----------------------------------
                                lambda Function

    ex:userdefined hof
'''
def cube(n):
    return n**3
def square(n):
    return n**2



lst=[]
def transform(fun,col):
    for i in col:
        result = i**2
        lst.append(result)

    return lst

l=[10,20,30,40,50]
print(transform(square,l))

print("_______________")
lst=[]
def transform(fun,col):
    for i in col:
        result = fun(i)
        lst.append(result)

    return lst

l=[10,20,30,40,50]
print(transform(cube,l))


#def cube(n):#simple helper function --> lambda function
#    return n**3
#lambda n:n**3
#def square(n):
#    return n**2
print("=================")
lst=[]
def transform(fun,col):#---->user defined (HOF)
    for i in col:
        result = fun(i)
        lst.append(result)#--> can convert to 1 line(using predefined Function)

    return lst

l=[10,20,30,40,50]
print(transform(lambda n:n**2,l))

print("+++++++++++++++++++++++++++")

m=map(lambda n:n**2,[10,20,30,40,50])
print(list(m))

print("---------------------------------")

print(list(map(lambda n:n**2,[10,20,30,40,50])))


'''
1) Map Function:
    -predefined HOF
    -Applies a given function to each item in iterable.
    -Returns a map object (an iterator).
    -"Used for applying common transformation logic to each else of iterable"
    syntax:
        map(function, iterable)
            -function ->shud takes one argument and return on value
            -iterable ->sequence (list, tuple , etc).

'''

def check_even(n):
    return n%2==0
lst=[]
def segregate(fun,col):
    for i in col:
        if fun(i): 
            lst.append(i)
    return lst

l=[3,8,12,13,19,22]
print(segregate(check_even,l))


print(list(map(lambda n:n%2==0,[3,8,12,13,19,22])))
'''
2)Filter Function:
    -filter out elements from an iterable based on a condition.
    -returns a filter object(an iterator)
    -filters only those elements wher the function returns True and adds it into filter object.
    Syntax:
        filter(function, iterable)
            -function -> thish function passed as a parameter must take 1 parameter and must return True or False.
            -iterable -> sequence

'''            
print(list(filter(lambda n:n%2==0,[3,8,12,13,19,22])))

'''
l=["lathik","YASHAS","Sagar","RAJ","SAI","cherian"]
'''

print(list(filter(lambda n:n.islower(),["lathik","YASHAS","Sagar","RAJ","SAI","cherian"])))

print(list(map(lambda n:len(n),["lathik","YASHAS","Sagar","RAJ","SAI","cherian"])))

print(list((lambda n:len(n),["lathik","YASHAS","Sagar","RAJ","SAI","cherian"])))

def add(a,b):
    return a + b

def compress(fun,col):
    result=0
    for i in col:
        result=result+i
    return result

l=[10,20,30,40,50]
print(compress(add,l))

def compress(fun,col):
    result=0
    for i in col:
        result=fun(result,i)
    return result

l=[10,20,30,40,50]
print(compress(add,l))

def compress(fun,col):
    result=0
    for i in col:
        result=fun(result,i)
    return result

l=[10,20,30,40,50]
print(compress(lambda a,b:a+b,l))

'''
3) Reduce Function
    -It's a function from functools module (from functools import reduce).
    -It applies a function "cumulatively" to the items of an iterable, reducing them to single value.
    Syntax:
        from functools import reduce
        reduce(function, iterable)

        function ->  a function that takes two arguments and shud return a Singlevalue
                    -takes two arguments
                    -returns one value
'''

from functools import reduce
print(reduce(lambda a,b:a+b,[10,20,30,40,50]))
print("++++++++++++++++++++++++++++++++++++")
print(reduce(lambda a,b:a*b,[10,20,30,40,50]))

l=[10,15,20,25,30,35]
#lst=filter(lambda n:n%2==0,[10,15,20,25,30,35])
print(list(map(lambda j:j**2,filter(lambda n:n%2==0,[10,15,20,25,30,35]))))
print(list(filter(lambda n:n%2==0,[10,15,20,25,30,35])))

'''
Comprehensions:
    -They  are python's way of writing loops that produce collections in a compact, readable form.
    -it combines => iteration+transformation+filtering


3 types of comprehensions:
--------------------------
    1)list comprehensions
        ->easier way to create lists (transformation+filtering)
    2)Set comprehensions
    3)dict comprehensions


    Syntax:(to create list comprehensions)
        l1 = [expression for variable in sequence] #iteration + transformation
'''
print("+++++++++++++++++")
ol = [2,3,4,5,6]

print([i+10  for i in [2,3,4,5,6]])

ol = ["Amy","Ben","Chad","Divya","Evan"]
#nl=[3,3,4,5,4]
print([len(i) for i in ["Amy","Ben","Chad","Divya","Evan"]])

'''                 (3)               (1)              (2)
    Syntax:    ----------  -----------------------  -----------
        l2  = [expression for variable in sequence if condition] #iteration+filtering+transformation+appending

'''
ol = [4,7,10,13,18]
#nl=[49,169]

print([i**2 for i in ol if i%2!=0])

ol = ["Amy","Ben","Chad","Divya","Evan"]
print([len(i) for i in ["Amy","Ben","Chad","Divya","Evan"] if len(i) > 3])

ol = ["Ms Amy","Mr Ben","Ms Chad","Mr Divya","Ms Evan"]
print([i for i in ["Ms Amy","Mr Ben","Mr Chad","Mr Divya","Ms Evan"] if i.startswith("Ms")])
print([i for i in ["Ms Amy","Mr Ben","Mr Chad","Mr Divya","Ms Evan"] if "Ms" in i])

'''
    Syntax:
        l3=[true_exp if condition else false_exp for variable in sequence] #iteration + filtering +Transformation + appending


'''                             
ol = [2,3,4,5,6,7]
#nl = 4,27,16,125,36]

print([n**2 if n%2==0 else n**3 for n in ol])                                                                                      
ol1 = ["Ms Amy","Mr Ben","Mr Chad","Mr Divya","Ms Evan"]
#nl = ["Beautiful", "Handsome", "Handsome", "Handsome", "Beautiful"]

print(["Handsome" if n.startswith("Mr") else "Beautiful" for n in ol1])


#nl = ["Beautiful Amy", "Handsome Ben", "Handsome Chad", "Handsome Divya", "Beautiful Evan"]
print(["Handsome"" "+n if n.startswith("Mr") else "Beautiful"" "+n for n in ol1])

'''
Set Comprehension
-----------------
1st syntax for Transformation only
s1 = {exp for var in collection}

2nd syntax for filtering only
s2 = {exp for varin collection if condition}

3rd syntax for Conditional transformation
s3={true_exp} if condition else false_exp for item in collection}

Dictionary Comprehension
-----------------
1st syntax for Transformation only general syntax
d1 = {key_exp: value_exp for item in iterable}
'''
l=[5,7,8,10,11]
#d={5:25.7:49,8:64,10:100,11:121}
print({i:i**2 for i in l})

l1=[5,7,8,10,11]
#d={25: 125, 49: 343, 64: 512, 100: 1000, 121: 1331}
print({i**2:i**3 for i in l1})

Candidates = ["Amy","Bennet","Chadwick","Divya","EvanJovelin"]
#d1={'Amy': 3, 'Bennet': 6, 'Chadwick': 8, 'Divya': 5, 'EvanJovelin': 11}
print({i:len(i) for i in Candidates})

Candidates = ["Amy","Bennet","Chadwick","Divya","EvanJovelin"]
#d1={'Amy': 3, 'Bennet': 6, 'Chadwick': 8, 'Divya': 5, 'EvanJovelin': 11}

print({i:i[::-1] for i in Candidates})


'''
d2 = {key_exp : value:exp for item in iterable if condition)
                                                ------------
                                                   True
'''
l2=[5,7,8,10,11]
print({i**2:i**3 for i in l if i%2!=0})


ol2 = ["Amy","Ben","Chad","Divya","Evan"]
ol2 = ["Ms Amy","Mr Ben","Mr Chad","Mr Divya","Ms Evan"]
print({i:"Handsome" for i in ol2 if i.startswith("Mr")})


'''
d3 = {key_exp :(True_exp if condition else False_exp ) for item in iterable}
                           ----------
'''
l4=[4,5,6,7,8,9]

print({i:(i**2 if i%2==0 else i**3 ) for i in l4})

d1 = {2:10,3:20,4:30,5:40,6:50}
print({i:(d1[i]**2 if i%2==0 else d1[i]**3 ) for i in d1})


d3 = {key_exp :(True_exp if condition else False_exp ) for k,v in d1.items()}
#using unpacking
print({var1:(var2**2 if var1%2==0 else var2**3) for var1,var2 in d1.items()})

'''
zip function:
------------
    -It is a predefined function in python that combines multiple iterables element. by element
    -It creates tuples of corresponding elements from each iterable.
    -Zip Function Accepts two or more iterables and "returns" Zip object "Iterator"

    Syntax:
        zip_obj = zip(iterable1, iterable2,.....)

    Note:Each element inside zipobject is a tuple
       ->zip stops at the shortest iterable
       ->it is used for mapping & pairing
'''



'''
