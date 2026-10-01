'''
Clousure
# closure is an inner function that remenbers and can access the variable from its enclosing
 (outer) function, even after the outer function has finished executing.

-steps needed to create a closure
1.create a outer function with a variable local to that puter function.
2.define an inner function that uses that outer variable(i.e, enclosing variable)
3.outer function RETURNS the inner function and this activates the closure.
NOTE: even though the outer function finishes its axecution, the
 outer function variable will be still remembered by inner function.


== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =


def outer():
    print("Outer function boody")
    a = 100

    def inner():
        print("inner function body", a)
    return inner


inner = outer()
inner()
inner()
inner()

#################
# -define an outerfunction called as get_color which contains enclosing variable called as
    color having red as the value.
   -define a nested function called show_color and showcase closure concept


   

def get_color():
    color="red"
    def show_color():
        print(color)
    return show_color

sol=get_color()
sol()

##########################################################

# -define an outerfunction called as counter which contains enclosing variable called as
    count having 0 as the value.
   -define a nested function called increament and showcase closure concept



def counter(count=0):
    def increament():
        nonlocal count
        count=count+1
        print(count)
    return increament

icr=counter()
icr()
icr()
icr()
################################################################################
################################################################################
'''