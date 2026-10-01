'''
Operators:
    -in python, an operator is a symbol or keywords
     that performs an operation on one or more operands (values or variable)
     and produces a result.

#############################

1.Arithmetic Operators:
    -used to perform mathematical operations.
    -Operators:
        -addition(+),substration(-),multiplication(*),division(/),
         floor division(//),modules(%),exponential(**).

print("Arithmetic Operators:")
a=100
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)#quotient with float value is given.
print(a//b)#quotient with int value is given.
print(a%b)#
print(3**2)
print(100**0.5)
print(100**0.3)
print("----------------------")
###########################

2.Assignment Operators:
    -used to assign values to variables, sometimes after performing some
     operations
    -Operators:
        -simple assignment(=),add and assign(+=),substract and assign(-=),
         Multiply and assign(*=),Divide and assign(/=),
         Floor divide and assign(//=),modules and assign(%=),
         power and assign(**=).

print("Assignment Operators:")
c=10
d=7
c+=d#c=c+d
print(c)
c-=d
print(c)
c*=d
print(c)
c/=d
print(c)
c//=d
print(c)
c**=d
print(c)
print("----------------------")

###########################
3.Relational Operators:
    -used compare values(and result in True and False).
    -Operator:
        -equal to(==),not equal to(!=),Greater than(>),Less than(<),
         Greater or equal(>=), less or equal(<=).

print("Relational Operators:")
e=111
f=110
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print("---------------------")
'''
##########################
'''
4.Logical Operators:
    -They are keywords
    -they used to ** evaluate conditions or combine contitions(True/Flase)**
    -Operators:
        and(true if both are True),or(True if at least one is true),
        not(Negation)
    -logical operators in python "dont always return True/False"
    -they return actual values ->short-circuit evaluation. 


print(True and True)
print(True and False)
print(False and True)
print(False and False)
print("----------")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print("----------")
print(not True)
print(not False)
print(8 and 16)
print(16 and 8)
print(8 or 16)
print(16 or 8)

A and B:
    -if A is truthy value, it returns B
    -if A is falsy value, it returns A
    default value is falsy value and non-default value is truthy values

print(1 and 0)
print(0.1 and 0.5)
print([] and [0.0])
print(True and "True")
print(None and "None")

A or B:
    -if A is truthy value, it returns A
    -if A is falsy value, it returns B

print(1 or 0)
print(0.1 or 0.5)
print([] or [0.0])
print("False" or "True")
print({} or {1,2,3})
############################


5.Identify Operators:
    -used to compare memory locations.
    -operators:
        -is(True if both refer to the same object).
        -is not(True if they dont refer to the same object).

a=100
b=a
print(a is b)
print(a is not b)
print("-----------")
l1=[10,20,30]
l2=[10,20,30]
print(l1 is l2)
print(l1 == l2)


6.Membership Operators:
    -used to test if a value exists is a sequeence(list,tuple,string,etc)
    -Operators:
        -in(True if value exists, not in(True if value does not exists)
        

l=[11,12,13]
print(12 in l)
print(12 not in l)

st="daniel"
print("d" is st)
print("D" is st)

d={47:"Rajmoli",28:"Yogesh",67:"Yashaswini"}
print("Raj" in d)
print(47 in d)
print("Raj" in d.values())
print("Rajmoli" in d.values())

7.Bitwise Operators:
    -work on binary numbers(bit-level operatons).
    -Bitwise operations are used to perform operations on the individuals bits
     of integers. they allow you to manipulate data at the
     binary level(0s and 1s).
    -operators:
        -&(bitwise AND),|(bitwise OR),^(bitwise XOR), ~(bitwise NOT),
         <<(left shift),>>(right shift).

'''
a=12#00001100
b=5#000000101
print(a & b)# bitwise AND, returns 1 if both bitss are 1.
print(a | b)#bitwise OR, returns 1 if atleast one of bits is 1.
print(a ^ b)#bitwise XOR, returns 1 if both bits are different.
print(~ a)#bitwise NOT, it inverts a bits 
          #Most significant Bit
print(a<<2)#<< bitwise leftshift, shifts the bits to left
           #var*2^(no of right shift positions)
print(a>>2)#<< bitwise rightshift, shifts the bits to right
           #var*2^(no of right shift positions)









