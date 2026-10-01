'''
# LAMBDA FUNCTION:
   -this function is small, anonymous function defined using lambda keyword.
       or
    -A lambda function is a function without a name, written in a single line, and used for
    short operations.
    -return shoud not be used
    NOTE:
        -LAMBDA function is best "when we need to pass simple helper function" for higher
        order function(function which takes other function as a parameter.)

        Syntax of lambda:
        lambda parameter: expression

    key rules:
        -no function name
        -no return keyword
        -expression result is returned automatically

    EXAMPLE:
    1.
    lambda a, b: a+b


v=lambda a,b: a+b
print(v(1,2))

w=lambda n:n**2
print(w(2))

e=lambda a,b,c,d:a+b-c+d
print(e(10,5,20,15))
'''
