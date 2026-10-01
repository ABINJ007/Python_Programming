'''
for i in range(1, 11):
    print("hello")

Looping = repeating a set of instructions multiple times until a condition is
          satisfied
     ->ALSO used to traverse Elements from collection

why to use loops:
    -Reduce code duplication (don't repeat same lines again and again)
    -Automate repetitive tasks (e.g., check 1000 files, send 1000 emails ,
     print 1000 numbers).
    -Work with collections(strings, lists, dicts ,etc).

Three Types of loops:
        -For Loop
        -While Loop
        -Nested For Loop
-----------------------------------------------------

For Loop:-->Known iterations
        -Best when you know in advance how many times to loop.
        -works with range() annd collections (list, tuple, string, dict).
        For loop Syntax:

            For varible in Sequence:
                #loop body(code to repeat)

        -variable -> takes on value from the sequence , at a time.
        -Sequence ->can be a range, list, tuple, string, or any iterable.
        -loop body->for each item or each value taken from the sequence, the
         indented for loop block runs
    
        


t = (1, 2, 3, 4, 5, 6, 7)
for i in t:
    print("Wednesday")

print("----------------------")

for i in range(1,51):
    print("Wednesday",i)

#print me numbers 4,8,12,16,20,24,28 uding for loop

for i in range(4,29,4):
    print(i)

    print("----------------------------------")

#l = [10, 20, 30 , 40 , 50, 60 , 70]
#for i in range(0,len(l),3):
 #s   print(l[i])

l = [10, 20, 30 , 40 , 50, 60 , 70]
for i in range(5,0,-2):
    print(l[i])
    
s={11,22,33,44}
#with for loop

d={1:10, 2:20, 3:30}
#for loop

st = "Aizen"
#for loop

for i in s:
    print(i)
for i in d.items():#bydefault when dict is used with for, we getkeys
    print(i)
for i in st:
    print(i,sep="\n",end="    ")


#when going thru each keys using for loop, if key matchs "yagami" print its value
d={"goku":"DragonBallz","yagami":"DeathNote","ichigo":"Bleach","migi":"parasyte"}


#for i in d:
 #   if i == "yagami":
  #      print(d.get(i))

for j in d:
    if "i" in j:
        print(d[j].upper())

2)while loop --> Unknown iterations
-Best when you don't know how many times you need to loop.
-Runs until condition becomes False.

while loop Syntax:
    Initialisation
    while Condition:
          -------------------
    ---->| #while loop block |
         |                   |
         | updation Logic    |
          -------------------
-condition --> Boolean expression (True/False)
-Loop runs as long as conditon is True

count = 80
while count>61:
    print(count)
    count = count  -3
l = [90, 80, 70, 60, 50, 40, 30, 20, 10]
i = 0
while i < 7 :
    print(l[i])
    i = i - 2
Loop control statements:
-----------------------
    1)break
    2)continue
    3)pass

            -how we can extra control or interruption during loop execution.
        
1)break ->it is a keyword in python.
        ->Stop the loop immediately and exits from the loop completely. Any statements inside the loop after "break" won't run.
        ->After that, the program continues after the foor /while loop block ie) remaining code outside for/while loop normally executes
        ->By doing this , it saves time by avoiding unnecessary looping execution

        Syntax of "break" in Loops:
        for variable in sequence
                if condition:
                    break  #exits the loop completely
                #rest of code
        while condition:
            id condition_to_stop:
                break      #exits the loop completely
                #rest of code

print("startS")
for i in range(45,68,1):
    if i%11 == 0:
        print(i)
        break
    
print("end")

print("______________________________________________________")

rolls=[497,19390,32,18,7,38,24]

for i in rolls:
    if i == 18:
        print(f"found:{i}")
        break

2)Continue -> it is a keyword in python
           -> Skip current iteration, Move to next iteration.
           -> It Doesn't stop the loop, only Skips that current iteration
           -> It will skip the remaining lines below the continue, insiderr the loop and jumps to the newxt cycle of the loop.
           -> continue helps ignore unwanted cases.

           Syntax:
               for variable in sequence:
               ----->if condition_to_continue:
                     ------>Continue

                     #Remaining Lines below  the continue inside loop will skip only if continue is Encounted.

for i in range(43,63):
    if i%2 == 0 and i%5==0:
        continue
    print(i)
    
print("_____________________________________________")
marks = [45, -74, 62, 74, 52, -48, 92, -35, 27, 93]
for i in marks:
    if i<0:
        continue
    print(i)


3)pass -> Do nothing(placeholder)
    -it is a keyword in python
    -Does literally nothing when executed.
    -Used as a placeholder when you haven't written the code yet.
    Syntax:
        for i in sequence:
            pass
        while condition:
            pass
   
if 5<6:
    pass
for i in range(3,6):
    pass
i=7
while i<9:
    pass
#instead of having empty block of code, use pass keyword in its place.
     
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
    -When you're looping, you often want to do something if the loop completed Normally (no break keyword id encountered.
    -If the loop was interrupted with break keyword, then else break block will Not be executed.
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


Nested Collection:
    A nested Collection means a collection (list, tuple, set, or dict) that contains another collection inside it.

    1)Nested List
    2)Nested Dict
    3)List of Dictionary
    JSON Stands for JavaScript Oject Notation
    It's basically a format to store and share structured data especially b/w client and server in web apps, APIs, etc.
    4)Dictionary of List(list inside dictionary) used in API or in dataframe in Pandas

    NEsted list:
        Having or placing  multiple list inside another list is known as Nested list

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


1)Nested List
2)Nested Dict
3)list of dictionary:
    JSON stands fro javaSript Object notation
    It's basically a format to store and share structured data-
    especially b/w client and server in web apps, APIs, etc.
4)DICTIONARY of LIST(list inside dictionary) used in API or in dataframe in pandas


company=[{'name':'Amy','salary':94000,'dept':'hr'},
         {'name':'Ben','salary':75000,'dept':'Research'},
         {'name':'Chad','salary':80000,'dept':'Sales'}
         ]
for i in company:
    print(i)

company={
    'names':["Amy","Ben","Chad"],
    'depts':["HR","Sales","Marketing"],
    'salaries':[94000,78000,84000],
    'ids':[101,113,124]
    }

#for i in company:
#    print(i)


for i in company['names']:
        print(i)
'''