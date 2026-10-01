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




print("______________________")


def add(a, b):
    return a + b


lambda a, b: a+b
print((lambda a, b: a+b)(10, 30))


def square(n):
    return n**2


lambda n: n**2
print((lambda n: n**2)(10))


def check_even(n):
    return n % 2 == 0


lambda n: n % 2 == 0
print((lambda n: n % 2 == 0)(20))

Calling a Lambda Function:
    Approach 1 - Assign to variable
    Approach 2 - Direct call
        syntax:
            lambda (para1,para2,para3,.....:Expression)(arg1,arg2,arg3,...)
                    -----------------------------------
                                lambda Function

    ex:userdefined hof



def cube(n):
    return n**3


def square(n):
    return n**2


lst = []


def transform(fun, col):
    for i in col:
        result = i**2
        lst.append(result)

    return lst


l = [10, 20, 30, 40, 50]
print(transform(square, l))

print("_______________")
lst = []


def transform(fun, col):
    for i in col:
        result = fun(i)
        lst.append(result)

    return lst


l = [10, 20, 30, 40, 50]
print(transform(cube, l))


# def cube(n):#simple helper function --> lambda function
#    return n**3
# lambda n:n**3
# def square(n):
#    return n**2
print("=================")
lst = []


def transform(fun, col):  # ---->user defined (HOF)
    for i in col:
        result = fun(i)
        # --> can convert to 1 line(using predefined Function)
        lst.append(result)

    return lst


l = [10, 20, 30, 40, 50]
print(transform(lambda n: n**2, l))

print("+++++++++++++++++++++++++++")

m = map(lambda n: n**2, [10, 20, 30, 40, 50])
print(list(m))

print("---------------------------------")

print(list(map(lambda n: n**2, [10, 20, 30, 40, 50])))
'''