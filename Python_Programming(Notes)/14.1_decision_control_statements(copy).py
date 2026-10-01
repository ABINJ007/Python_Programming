'''
Dicision control statements:
    -they are used to control the flow of programme execution based on conditions
    -they allow the programme to dicide what to execute depending on
     True/False conditions.

Indentation:
    -providing spaces at the begining of the line within the (one tab space
     or four line space) 
    -in python indentation is mandatory to define any block of code.
    -if,funtion,for loop block etc

Types:
-if statements:
        -it is a keyword.
        -it executes a block of code only when the condition is True.
        -use if statement when we need to test the single condition.
        -Syntax:
            -if condition:
                #if block of code.
    -if-else:
    -if-elif-else
    -match-case
    -nested-if
    

#if-statement:

marks=int(input("Enter your marks: "))

if marks>50:
    print("Congragulations")
print("END")


num=int(input("Enter the number: "))
if num>0:
    print("Positive Number")
print("end")


students={21:"abin",45:"joseph",56:"daniel"}
#check if daniel is in the student list, if true print("danger")

if "joseph" in students.values():
    print("Danger")


##############################################################################
##############################################################################
2. if-else:
    -else is also a keywords
    -only when the condition is true if block will be executed.
     other wise else block will be executed.
    -else keywords is nit followed by the condition and it should be
     written at the last.
    -use if else when you want only two possiblities/two choices.
    -Syntax:
        -if condition:
            #if block
         else:
             #else block


#except marks from the user
#check if marks greter that 35, if true print("congr") else print("sorry")

marks=int(input("Enter your marks: "))

if marks>35:
    print("Congragulations")
else:
    print("Congragulation your successfully failed")


#except name from the user
#check if name lenght greter that 8, if true print("user valid") else print("inval")
name=input("Enter your name: ")
if len(name)>8:
    print("Valid")
else:
    print("invalid")


#except a sentence from the user
#check if sentence more than 4 words,if true print("valid") else print("invalid")
str=input("Enter a sentence: ")
sen=len(str.split())
print(sen)
if len(str.split())>4:
    print("valid")
else:
    print("invalid")

############################################################################
############################################################################

3. if-elif-else:-
    -it is a keyword in python.
    -used when there are multiple conditions to check ans only the first
     matching conditions ans its bloack will wxecute.
     use when you want" " many choices but only one should apply"".
    -elif is followed by a condition and can be repeated as many times as
     needed.
    -else can come at last, and only once and is optional.
    -Syntax:
        -if conditions:
            #if block of code
         elif:
            #elif 1 block of code
         elif:
            #elif 2 block of code
         else:
            #else block of code


#accept temperature from the use
#Hot weather if temp exceeds 35
#warm weathre if temp is between 15 and 35
#print cool weather if temp is between 8 to 14
#PRINT cold weather if temp is below 8


temp=float(input("Enter the temperature: "))

if temp>35:
    print("Hot weather")
elif temp>=15 and temp<=35:
    print("Warm weather")
elif temp>=8 and temp<=14:
    print("cool weather")
else:
    print("cold weather")


#accept marks from the use
#A grade if marks exceeds 90
#B grade if above 70 and 90
#C grade if above 50 and 70
#D grade if above 35 and 50
#print fail if below 35
        
marks=int(input("Enter the marks: "))

if marks>=90 and marks<=100:
    print("A Grade")
elif marks>=70 and marks<90:
    print("B Grade")
elif marks>=50 and marks<70:
    print("C Grade")
elif marks>=35 and marks<50:
    print("D Grade")
elif marks<35 and marks>=0:
    print("Fail")
else:
    print("Invalid")
       OR
if marks>=0 and marks<=100
    if marks>=90 and marks<=100:
        print("A Grade")
    elif marks>=70 and marks<90:
        print("B Grade")
    elif marks>=50 and marks<70:
        print("C Grade")
    elif marks>=35 and marks<50:
        print("D Grade")
    elif marks<35 and marks>=0:
        print("Fail")
else:
    print("invalid")

##########################################################################
##########################################################################
4.match case;
    -introduced in python 3.10, match case is pythons version of switch,
     but much more powerful
    -syntax:
        -match expression:
            case pattern1:
                block
            case pattern2:
                block
            case _:
            default block



import keyword
print(keyword.softkwlist)

#acccept the weekday num from user
#   ->using matchcases, if the weekdaynumber is 1,Monday to be printed



weekday=int(input("Enter the weekday number: "))

match weekday:
    case 1:
        print("mon")
    case 2:
        print("tue")
    case 3:
        print("wed")
    case 4:
        print("thur")
    case 5:
        print("fri")
    case 6:
        print("sat")
    case 7:
        print("sun")
    case _:
        print("Invalid")


###########################################################################
###########################################################################
nested-if
    -pllaceing an if inside another if "to check multiple levels of conditions."
    -use when you need to check  condition inside another condition.
    -syntax:
        -if outer_condition:
            if inner_condition:
                #inner if block code
            elif:
                #inner elif block
            else:
                #inner else block
         else:
             #outer else block


#design a nested condition where in accept username and check if its correct
#-only if its correct, accept the password, else print wrong username"
#-then check if its the correct password,if correct print login succesful,
    else print "invalid password"



username=input("Enter the username: ")
if username=="daniel":
    print("username correct")
    password=input("ENter password")
    if password=="dan123":
        print("login success")
    else:
        print("invalid password")
else:
    print("Wrong password")

##############################################################################
###########################################################################
6, conditional operation:
    -a shorthand way of writting if-else in one line.
    -Syntax:
        -result = true.exp if condition else false.exp.

num = 40

result="pos" if num>0 else "neg"
print(result)


#check if kiran is present in the list if present, print length of the list
#if not present print "not found"

l=["mohan","rohini","kiran"]

res=len(l) if "kiran" in l else "Not found"
print(res)

'''





































