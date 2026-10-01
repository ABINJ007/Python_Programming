'''
Operators:
In python, an operator is a symbol or keyword that performs an operation on one or more operands (values or variables) and produces a result."
1)Arithmetic Operators>:
                ->Used to perform mathematical operations.
                ->Operator       Meaning
                                 Addition(+)
                                 Substraction(-)
                                 Multiplication(*)
                                 Division(/)(quotient with float value is given)
                                 Floor Division(//)(Quotient  with in value is given)
                                 Modulus(%)(remainder)
                                 Exponentiation(**)
'''
print("-------------------------")
a = 101
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)  # quotient with float value is given
print(a//b)  # Quotient with int value is given
print(a % b)
print(100**0.33)

##############################
'''
2)Assignment Operators>:
                    ->Used to assign values to varibles, sometimes after performing some operations.
                    Operator            Meaning
                       =                Simple assignment
                      +=                Add and assign
                      -=                Subtract and assign
                      *=                Multiply and assign
                      /=                Divide and assign
                     //=                Floor and assign
                      %=                modulus and assign
                     **=                power and assign
'''
print("--------------------------------")


a = 100
b = 79
a += b  # a=a+b
print(a)

a -= b  # a=a-b
print(a)

a *= b  # a=a*b
print(a)

a /= b  # a=a/b
print(a)

a //= b  # a=a//b
print(a)

a %= b  # a=a%b
print(a)

a **= b  # a=a**b
print(a)
################################
'''

3)Relation Operators>:
                    ->Comparison (Relational) Operators used to compare values ( and result is True or False).
                    ->Operator          Meaning
                        ==              Equal to
                        !=              Not Equal to
                        >               Greater than
                        <               Less than
                        >=              Greater or equal
                        <=              Less or equal
'''
###################
'''
4)Logical Operators>:
                    ->They are used to evaluate conditions or combine conditions(True/False).
                    ->Operator          Meaning
                       and              True if both are true
                       or               True if atleast one is true
                       not              Negation
'''
#######################################

print("=============================")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print("=============================")

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("=============================")
print(not True)
print(not False)

# Logical operators in Python don't always return True/False.
# They return actual values ->Short-Circuit Evaluation.

print(8 and 16)
print(16 and 8)
print(8 or 16)
print(16 or 8)
'''
A and B :    1) If A is Truthy value, it returns B.
             2) If A is Falsy Value, It immediately returns A.
             and stop when 1 st Falsy value is Found.
'''

print(1 and 0)
print(0.1 and 0.5)
print([] and [0.0])
print(True and "True")
print(None and "None")

'''
A and B :    1) If A is Falsy Value, It immediately returns A.
             2) If A is Truthy value, it returns B.
             and stop when 1st Truthy value  is Found.
'''
print(1 or 0)
print(0.1 or 0.5)
print([] or [0.0])
print(False or "True")
print({} or {1, 2, 3})


#########################################
'''

5)Identity Operators>:
                    ->Used to compare memory Location.
                    ->Operator          Meaning
                       is               True if Both refer to the same object.
                       is not           True if they don't refer to the same object.
'''

print("========================")

a = 200
b = a
print(a is b)
print(a is not b)
print("========================")
l1 = [10, 20, 30]
l2 = [10, 20, 30]
print(l1 is l2)
print(l1 == l2)
##########################
'''
6)Membership operators>:
                    ->used to test if a value exists i a sequence (list, tuple , string,  etc.).
                    ->Operator          Meaning
                       in               True if value exists.
                       not in           True if value does not exist.

'''
###########################
print("========================")


st = "Raghavendra"
print("Ra" in st)
print("Ru" in st)

print("========================")

dict = {47: "Rajmouli", 28: "yogesh", 67: "Yashaswini"}
print(47 in dict)
print("Raj" in dict)
print("yog" in dict.values())
print(67 in dict.keys())
print("Yas" in dict.keys())
print("Yohesh" in dict.items())


##########################
'''
7)Bitwise operators>:
                    ->Work on binary Numbers (bit-Level operations).
                    ->Bitwise operators are used to perform operstion on the individual bits of integers. They allow you to manipulate data at the binary level( 0s and 1s).
                    ->Operator          Meaning
                       &                Bitwise AND
                       |                Bitwise OR
                       ^                Bitwise XOR
                       ~                Bitwise NOT (1's complement)
                      <<                Left shift (add zeros)
                      >>                Right shift
7.1)& bitwise AND operator returns 1 if both bits are 1.
7.1)| bitwise OR operator returns 1 if atleast one of bits is 1.
7.1)^ bitwise XOR operator returns 1 if both bits are different.
7.1)~ bitwise NOT operator invertes the bits.
7.1)<< bitwise Leftshift operator shifs the bits to left.


'''
###########################
print("==============================================")

a = 12  # --> 0 0 0 0 1 1 0 0

b = 5  # --> 0 0 0 0 0 1 0 1


a = 12  # --> 0  0  0  0  1  1  0  0
#    1  1  1  1  0  0  1  1
#    ----------------------
#  -128+64+32+16+       2+1   ====-13
#
l = ['00000101', '01000010']
l2 = ['00000101', '01000010']
print(l is l2)
print(l == l2)
print(l)
