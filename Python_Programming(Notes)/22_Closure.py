'''
Closure:
    A Closure is an inner function that remembers and can access the variables
    from its enclosing(outer) function, even after the outer function has
    finshed executing.

    steps needed to create a closure:
    1)Create an outer Function with a variable local to that outer function.
    2)Define an inner Function that uses that outer Variable
    3)Outer Function "Returns" the inner function and this activites the closure.
    NOTE: even though the outer functiion finishes its execution, the outer
    function's variables will be still remembered by inner function

    Usage:
    1)Used in Decorates
    2)Access Control
    3)cashing

def outer():
    print("outer function body")
    def inner():
        print("inner function body")
    return inner
outer()

define an outerfunction called as get_colour which contains enclosing variable
called as colour having read as the value
define a nested Function called show_colour and showcase closure concept

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
