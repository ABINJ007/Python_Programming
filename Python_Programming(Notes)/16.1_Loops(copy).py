'''
looping
        -repeating a set of instruction multiple times until a condition is
         is satisfifed.
        -also used to traverse elements from collection

    -why to use loops:
        -reduce code duplication(dont repeat same lines agai nad agian).
        -automated repetitive tasks(e.g., chceck 1000 files, send 1000 emails
         print 1000 numbers).
        -work with collections(string,list,dict, etc.).

    -types of loop(3 types)
        -for loop
        -while loop
        -nested for

#############################################################################
#############################################################################
1. for loop:
    -Known iterations.
    -best when you know in advance how many times to loop.
    -works with range() and collection(list,tuple,string,dict).

    -syntax:
        -for variable in sequence:
            #loop body(code to repeat)

    -variable->takes one value/element from sequenve at a time.
    -sequence->can be a range, list, tuples, string, any iterable.
    -loop body->for each item or each value taken from the sequence,
     the indented for loop block runs.

l=[10,20,30,40,50,60,70]
for i in l:
    print("wed")

for i in range(1,51,1):
    print("wed")

for i in range(1,51,1):
    print("wed",i)


#print me numbers 4,8,12,16,20,24,28    
for i in range(4,29,4):
    print(i)

###################
l=[10,20,30,40,50,60,70]
for i in range(0,len(l),3):
    print(l[i])


##################
l=[10,20,30,40,50,60,70]

for i in range(5,0,-2):
    print(l[i])
   
##################
s={11,22,33,44}#unordered manner
for i in s:
    print(i)


d={1:10,2:20,3:30}
for i in d.values():#by default when dict is used with for loop we get keys
    print(i)


for i in d.items():
    print(i)

st="aizen"
for i in st:
    print(i)


###########################################
#when going thru each keys using for loop, if key matchs "yagami" print its value
d={"goku":"DragonBallz","yagami":"DeathNote","ichigo":"Bleach","migi":"parasyte"}

for i in d:
    if i=="yagami":
        print(d[i])

##########################################
#when you are going throu each keys using loop, if key contains "i", print the
#uppercase value of it
d={"goku":"DragonBallz","yagami":"DeathNote","ichigo":"Bleach","migi":"parasyte"}
for i in d:
    if "i" in i:
        print(d[i].upper())

#############################################################################
#############################################################################

2. while loop
        -unknown iterations
        -best when you dont know how many times you need to loop.
        -runs until condition becomes False.

    -syntax:
        -while condition:
            #while loop block
            updation logic

        -condition->boolean expression(True/Flase)
        -loop runs as long as condition is True.

count=0
while count<5:
    print("hello")
    count=count+1


count=10
while count<16:
    print("hello")
    count=count+1

#print me number from 51 to 60 including using while loop

count=51
while count<61:
    print(count)
    count=count+1


#print me number from 87,89,91,93,95 including using while loop
count=87
while count<96:
    print(count)
    count=count+2

#print me number from 8,7,6,5,4,3,2 both including using while loop
j=8
while j>1:
    print(j)
    j=j-1
    
#print me number from 80,77,74,71,68,65,62 both including using while loop
j=80
while j>61:
    print(j)
    j=j-3


l=[90,80,70,60,50,40,30,20,10]
#i want to print 90,70,50,30 using while loop

count=0
while count<7:
    print(l[count])
    count=count+2

##########################################################################
##########################################################################
##########################################################################

Loop control statements:
-----------------------
    1)break
    2)continue
    3)pass

            -how we can extra control or interruption during loop execution.
        
1)break ->it is a keyword in python.
        ->Stop the loop immediately and exits from the loop completely.
          Any statements inside the loop after "break" won't run.
        ->After that, the program continues after the foor
         /while loop block ie) remaining code outside for/while loop
         normally executes
        ->By doing this , it saves time by avoiding unnecessary looping
         execution

        Syntax of "break" in Loops:
        for variable in sequence
                if condition:
                    break  #exits the loop completely
                #rest of code
        while condition:
            id condition_to_stop:
                break      #exits the loop completely
                #rest of code



for i in range(2,8):
    print(i)
    break

#when u r printing numbers from 51 to 70,if you come acroos ant number divisible
by 11, i want to stop imedieatly and come out of the loop.



print("start")
for i in range(51,71,1):
    if i%11==0:
        break
    print(i)
print("end")

#when u r going thru numbers from 45 to 67,if you come acroos ant number divisible
by 11, i want you to print only that number and stop imedieatly and come out of
loop.

print("start")
for i in range(51,71,1):
    if i%11==0:
        print(i)
        break    
print("end")

#when itereating thru each roll number, search if there is 18 as rollnumber, if
#YES print rollnumber 18 found and stop the loop.
rolls=[497,19390,32,18,7,38,24]
for i in rolls:
    if i==8:
        print(i)
        break

###################################################################
####################################################################
2.continue:
        -its a keyword.
        -skip current iteration,move to next iteration.
        -it doesnt stop the loop,only SKIPS THAT current iteration.
        -it will SKIP the remaining lines below the continue, inside the
         loop and jumps to the next cycle of the loop.
        -continue helps ignore unwanted cases.

        -Syntax:
            -for variale in sequence:
                if condition_to_continue:
                    continue
         #remaining lines below the continue loop will skip only if contiiue
          is encounted.

for i in range(2,20):
    continue
    print(i)               


#when printing numbers ffrom 43 to 63, i want you to skip any number which
 divisible by 3, other numbers shud be printed


for i in range(43,63):
    if i%3==0:
        continue
    print(i)

#any number divisble by 2 AND 5 then skip

for i in range(43,63):
    if i%2==0 or i%5==0:
        continue
    print(i)


marks=[45,-74,62,74,52,-48,92,-35,27,93]

for i in marks:
    if i<0:
        continue
    print(i)
    

#when iteration thru each names,
#if the no of charaters is less than 5,skip them
#if the no of character is greater than 5,print them
#if no od charachter is equal to 5, stop the loop and come out
names=["nandan","raghu","basu","raj","om","shravani","daniel"]


###########################################################################
###########################################################################

Nested For Loop:
---------------
    -One For loop inside another for loop.
    -when outer loops runs once, The inner loop runs fully every time.
    -used when you want all combinations from two groups.
    Syntax:
        for variable in sequence1:
        ----->for variable2 in sequence2:  <-----outer for block
        --------->inner for loop Block
        


for i in range(2,5,1):
    for j in range(1,4,1):
        print(f'{i} * {j} = {i*j}')

M=["dosa","idle","puri"]
S=["chutney","sambar","aloocurry"]
for Ms in M:
    for Ss in S:
        print(f"{Ms} {Ss}")



For Else Block:
---------------
    -When you're looping, you often want to do something if the loop completed
     Normally (no break keyword id encountered.
    -If the loop was interrupted with break keyword, then else break block
     will Not be executed.

    Syntax:
        for variable in sequence:
            for loop block:
        else:
            #else block will run once at the last, when the above loop completes nnormally without executing break.
    -The else block runs only if loop completes normally(no break)
    -If the loop was
    

Rollno = [77,72,7,73,79,72,71]
Rol = int(input("Enter RollNO:"))
for R in Rollno:
    if R == Rol:
        print("Found")
        
else:
    print("not")



################################################################################
#################################################################################
Nested Collection:
    A nested Collection means a collection (list, tuple, set, or dict) that
    contains another collection inside it.

    1)Nested List
    2)Nested Dict
    3)List of Dictionary
     JSON Stands for JavaScript Oject Notation
     It's basically a format to store and share structured data especially b/w
     client and server in web apps, APIs, etc.
    4)Dictionary of List(list inside dictionary) used in API or in dataframe in Pandas

    Nested list:
        Having or placing  multiple list inside another list is known as
        Nested list

l = [["Amy", 23, 94000],["Ben", 44, 75000],["Chad", 12, 80000]]
for i in l:
    if i[2]>90000:
        print(i[0].upper())
        i[0] = i[0].upper()
        print(l)

Nested Dictionary:  
----------------

company={'emp1':{'name':'Amy','salary':94000,'dept':'hr'},
         'emp2':{'name':'Ben','salary':75000,'dept':'Research'},
         'emp3':{'name':'Chad','salary':80000,'dept':'Sales'}
         }
print(company)
print("_______________________________________________")
for i in company.values():
    #if i["dept"] == "HR" or i["dept"] == "hr":
    #if i["dept"].upper() == "HR" :
    if i["dept"].lower() == "hr" :
        #print(company[i]['name'])
        
        #print(company.get(i).get("name"))
        print(i["name"])
        
for i in company.values():
    print(i['name']['

##############################################################################
##############################################################################

3)list of dictionary:
    JSON stands fro javaSript Object notation
    It's basically a format to store and share structured data-
    especially b/w client and server in web apps, APIs, etc.



company=[{'name':'Amy','salary':94000,'dept':'hr'},
         {'name':'Ben','salary':75000,'dept':'Research'},
         {'name':'Chad','salary':80000,'dept':'Sales'}
         ]
for i in company:
    print(i)


################################################################################
############################################################################33#

4.Dictionary of list:
    -used in api or in dataframes in pandas.
    
    

company={
    'names':['Amy','Ben','Chad'],
    'depts':['HR','Sales','Marketing'],
    'salaries':[94000,78000,84000],
    'ids':[101,113,124]
    }

for i in company:
    print(i)

company={
    'names':['Amy','Ben','Chad'],
    'depts':['HR','Sales','Marketing'],
    'salaries':[94000,78000,84000],
    'ids':[101,113,124]
    }
for i in company['names']:
    print(i)
print("-----------------------------------")
for i in range(0,3):
    print(company['names'][i])
'''   





