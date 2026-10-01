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
'''