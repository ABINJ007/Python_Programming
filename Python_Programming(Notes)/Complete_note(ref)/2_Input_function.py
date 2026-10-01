
#eval() is a build in python function that evaluates (executes) a string as a python expression and returns the result.
#it can auto-decide the datatype
'''
Syntax:
    result = eval("Expression written inside string")
'''
#Expression :
# A Python expression
'''
a = 200
b = 23

exp = eval("a-b+50")
print(exp)
l = [12, 34, 34]
exp1 = eval("len(l) + 24")
print(exp1)
'''

'''
exp2=eval("False")#automatically performs typecasting and usefull for accepting boolean value from use and evaluating expression.
print(exp2)
print(type(exp2))
'''
'''
Concatenation

It means joining two or more strings together to make one continuous string.
You can concatenate strings using the + Operator

syntax:
newstring="string1" + "sting2" + "String3" + .......

'''

'''
player_name= input("Enter the player name:")
age = int(input("Enter the age:"))
average = float(input("Enter the Average:"))
team = input("Enter the Team Name:")
is_genius =eval(input(""))
print(player_name + " whose age is " +str(age) + " and average is " +str(average) + " plays for " +team+ " is a " +str(is_genius)+".")
'''
#string Formatting=>
'''
means Inserting variables or values into a string template in a clean and readableway, using + Multiple times.
1st way to do is Using f-strings:
    syntax:
        reference=f"string with a "placeholder"(placeholder should not be empty) {vairablename}"
    Positives:
        -Automatically converts types(no need for str())
        -Easier to read
        -Supports expressions inside {}
'''

#print(f"{player_name} whose age is {age} and average is {average} plays for {team} is a {is_genius}

num1 = 50
num2 = 28
result = num1 + num2
print(f"Addition of {num1} and {num2} is {result}.")


statement = f"hello {num1}{num2}"
print(statement)

'''
2nd using format() Method
syntax:
    "string with {} placeholders" .format(valuesplayer_name= input("Enter the player name:")

player_name= input("Enter the player name:")
age = int(input("Enter the age:"))
average = float(input("Enter the Average:"))
team = input("Enter the Team Name:")
is_genius =eval(input(""))
hello ="{} whose age is {} and average is {} plays for {} is a {} genius.".format(player_name,age,average,team,is_genius)
print(hello)
'''
'''
print Function
   
it is a pre-defined function in python which is used to display output on the console or the screen.
print function helps the programmer see the results of program/code Execution.
print function has 2 Default Arguments
    1)sep:
        syntax:
            print(v1, v2, v3, sep=' ')
            Whenever Multiple values are to be printed using print function, the value of the separter will be printed in  b/w those values
            The default value of sep is space.
            If there are N values to be printed the sep value will be printed n-1 times in b/w them.
'''
            #sep=" "
print(10,20,30,40,50, sep="07")
print(10,20,30,40,50, sep="\n")
"""           
    2)end:
        syntax:
            print(v1,v2,v3,end='\n')
            when Multiple or single values is printed using print Funciton at the End the value of the End argumment will be executed or printed.
            The default value of end is "\n".
            If there are N values to be printed the end argument value will be printed only once at the end.
                                                                                            ----                    
"""
print(11,22,33, sep=" ", end="@")
print(44, end=" ")
print(55,66, sep="\n")
print("----------------------")

print(10,20,30,sep="\n",end=" ")
print(40,sep="", end="@")
print(50,60,70,sep="\n",end="\n")
print("stop")

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
print(a/b)#quotient with float value is given
print(a//b)#Quotient with int value is given
print(a%b)
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


a=100
b=79
a+=b#a=a+b
print(a)

a-=b#a=a-b
print(a)

a*=b#a=a*b
print(a)

a/=b#a=a/b
print(a)

a//=b#a=a//b
print(a)

a%=b#a=a%b
print(a)

a**=b#a=a**b
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

#Logical operators in Python don't always return True/False.
#They return actual values ->Short-Circuit Evaluation.

print(8 and 16)
print(16 and 8)
print(8 or 16)
print(16 or 8)
'''
A and B :    1) If A is Truthy value, it returns B.
             2) If A is Falsy Value, It immediately returns A.
             and stop when 1 st Falsy value is Found.
'''
             
print(1 and 0 )
print(0.1 and 0.5)
print([] and [0.0])
print(True and "True")
print(None and "None")

'''
A and B :    1) If A is Falsy Value, It immediately returns A.
             2) If A is Truthy value, it returns B.
             and stop when 1st Truthy value  is Found.
'''
print(1 or 0 )
print(0.1 or 0.5)
print([] or [0.0])
print(False or "True")
print({} or {1,2,3})     

    
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
l1 = [10, 20 ,30]
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

dict = {47 : "Rajmouli", 28 : "yogesh", 67 : "Yashaswini"}
print(47 in dict)
print("Raj" in dict)
print("yog" in dict.values())
print(67 in dict.keys())
print("Yas" in dict.keys())
print("Yohesh"in dict.items())


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

a = 12 #--> 0 0 0 0 1 1 0 0

b = 5  #--> 0 0 0 0 0 1 0 1


a = 12 #--> 0  0  0  0  1  1  0  0
       #    1  1  1  1  0  0  1  1
       #    ----------------------
       #  -128+64+32+16+       2+1   ====-13
       #
l = ['00000101', '01000010']
l2 = ['00000101', '01000010']
print(l is l2)
print(l == l2)
print(l )
'''
Decision Control Statements:
They are used to control the follow of program Execution based on Conditions.
THey allow the program to decide what to Execute depending on True/False Conditions.

Indentation:
providing spaces at the begining of the line(One tab space or four line space).
In python indentation is mandatory to define any block of code.(if blocks , funtion block , for loop block etc).

Types:
If Statement(Condition):
If else
IF - elif - else
If - elif - else - match_case - Nested if

1)If statement:
    If is a keyword in Python.
    It executes a block of code only when the condition is True.
    Use if statement when we need to test a single condition.

    Syntax:
            if Condition :
               ---------
            -->|#if block|
               |    of   |
               |   code  |
'''
'''
marks = int(input("Enter Your Marks:"))
print("Start")
if marks>90:
    print("A grade")
print("end")
'''
'''
#num = int(input("Enter any number:"))
num = int(input("Enter any number:"))
print("Start")
if num>0 :
    print("Positive")
print("End")
'''
'''
Students = {7 : "Daniel", 8 : "Cherian" , 9 : "Adhwith"}
if "Cherian" in Students.values():
    print("Danger")
'''
######################
'''
Else Statement:
    -->Else also a Keyword in Python.
    -->Only when the Condition is True if block will Executed otherwise else will be Executed.
    -->Else keyword not follow by a condition and it should be written at the last.
    -->Use if else when you want only two possiblities / Two choices.
    Syntax:
            if Condition :
               ---------
            -->|#if block|
               |    of   |
               |   code  |
            else:
            -->|#else block|
               |    of     |
               |  Code     |
'''

'''
marks = int(input("Enter Your Marks:"))
print("Start")
if marks>30:
    print("Congrats")
else:
    print("Congrats you are Failed")
print("end")
'''
'''
name =input("Enter Your Name:")
print("Start")
if len(name)>8:
    print("Username valid")
else:
    print("Invalid username")
print("end")

#Accept a sentence from the user
#if the sentence has more than 4 words, print " valid Sentence
#else print "Invalid Error"

sen = input("Enter Sentence:")
#sen_len =len(sen.split())
if len(sen.split())>4:
    print("valid Sentence")
else:
    print("Invalid Error")

3)If-elif-else ladder:
            -->elif is a keyword in Python
            -->Use when there are multiple conditios to check and only the first matching condition and its block will execute.
            -->use when you want "" many choices but only one should apply""
            -->elif is followed by a condition and can be repeated as many times as needed.
            -->else must come last, and only once.
            Syntax:
                  if Condition 1:
                     ---------
                  -->| #if block  |
                     |     of     |
                     |   code     |
                  
                  elif condition 2:
                  -->|elif 1 block|
                     |    of      |
                     |   code     |
                  elif condition 3:
                  -->|elif 2 block|
                     |    of      |
                     |   code     |


?accept temperature from user
?print hot weather if temps exceeds 35
?print warm weather if temp is between 15 to 35
?print cool weather if temp is between 8 to 14
?print cold weather if temp is below 8

tem = float(input("Enter the Temperature:"))
if tem>=35:
    print("Hot weather")
elif tem>=15 and tem<=35:
    print("Warm weather")
elif tem>=8 and tem<=14:
    print("cool weather")
elif tem<=8:
    print("cold weather")
else:
    print("invalid value")


?Accept marks from user
print A grade if marks exceeds 90
print B grade if above 70 and below 90
print c grade if above 50 and below 70
print D grade if 35 and below 50
print Fail if below 35

marks = int(input("Enter the Marks:"))
if marks>=0 and marks<=100:
    if marks>=90 and marks<=100:
        print("A grade")
    elif marks>=70 and marks<90:
        print("B grade")
    elif marks>=50 and marks<70:
        print("C grade")
    elif marks>=35 and marks<50:
        print("D grade")
    elif marks<35 and marks>=0:
        print("Fail")
else:
    print("Invalid value")

4) Introduced in Python 3.10, match case is pythons version of switch, but much more powerfull.
  it mataches structure not values 
Syntax:
    -Match Expression:
        case pattern1:
                block
        case pattern2:
                block
        case pattern3:
                default block

'''
import keyword
print(keyword.softkwlist)


'''
Accept the weekday num from user
--> Using matchcase, if the weekday number is 1, Monday to be printed

if the weekdaynumber is 1, Monday to be printed
if the weekdaynumber is 2, Tuesday to be printed
if the weekdaynumber is 3, Wednesday to be printed
if the weekdaynumber is 4, Thursday to be printed
if the weekdaynumber is 5, Friday to be printed
if the weekdaynumber is 6, Saturday to be printed
if the weekdaynumber is 7, Sunday to be printed

weekday = int(input("Enter the Weekday Numbers:"))
match weekday:
              case 1:
                  print("Monday")
              case 2:
                  print("Tuesday")
              case 3:
                  print("Wednesday")
              case 4:
                  print("Thursday")
              case 5:
                  print("Friday")
              case 6:
                  print("Saturday")
              case 7|0:
                  print("Sunday")
              case _:
                  print("Invalide weekday number Entered")

Nested-if:
---------
        Can place an if inside another if " to check multiple Levels of Conditions".
        Use when you needs to check a Condition inside another condition.
        -Syntax:
                if Outercondition:
                    if innercondition:
                        #inner if block
                    else:
                        #inner else block

                else:
                    #inner else block


?Design a nested condition where in accept username and check if its correct
-only if its correct,accept the password, else print "wrong username"
-then check if its the correct password, if correct print login successful,
    else print "Invalid Password"


#Username ="Cherian"
#password ="cherian@123
Username = input("Enter the Username":)
passw = input("Enter the password":)
if user==Username:
    print("Username correct")
        if password == passw:
            print("Login Sucessful")
        else:
            print("

6)Conditional Expression(Ternary operator)
       ->A Shorthand way of writing if-else in one line
       ->Syntax:
               Result = true_exp If condition else false_exp
               

num = 40
if num>0:
    print("Postive")
else:
    print("Negative")
print("---------------------")

result = "PositveNumber" if num>0 else "NegativeNumber"
print(result)

l = ["Mohan", "Rohini", "kiran"]
if "kiran" in l:
    value =len(l)
    print(value)
else:
    print("not found")
print("---------------------")

result = len(l) if "kirana" in l else "Not Found"
print(result)

Range:
----- -->Range is implemented as a class.
      -->When you call range(), you're actully creating a range object (an instance of the range class).
      -->it's an immutable sequence type like tuple or string
      syntax:
              -range(stop)
              -range(start, stop)
              -range(start, stop, step)
                       |      |     |
                      DV=0   none   DV=1(Default value)
Usage of range():
        ->when you need a sequence of numbers(for countin, indexing, iteration).range() doesn't actually create all the numbers - it just remembers how to generate them.
        ->when you want to loop a specific number of times
        ->when you wnat to avoid creating large lists in memory.

Features of range:
    1)Immutable --> once created, it cannot be changes.
    2)Lazy/Memory Efficient -->Doesn't generate all numbers at once. It stores only :
                -start
                -stop
                -step
        and generates numbers when needed on demand.
    3)Iterate -> Can be used in for loops.
    4)Supports indexing  & slicing.
'''

result=range(1, 8, 1)
print(result)
print(type(result))

#Explicit typecasting on range object
print(list(result))
print(tuple(result))
print(set(result))
print(str(result))

result1=range(11, 46, 11)
print(list(result1))

result2=range(1, 12)
print(tuple(result2))

result3=range(-1, -10 , -2)
print(list(result3))

print(list(range(-9, 2, 2)))








