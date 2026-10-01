#input funtion
'''
-it si a built in function in python which is used to take input from the user through keyboard.
-whatever the user enters is always recieved in the form of string.
-SYNTAX:
    input("Any Message/Prompt display to user").

-where and why the input is used.
    -when the user and the programmer plans to write interactive
    programs that takes data from the external entity, we use input funtion.
    
'''
'''
name = input("Enter your name: ")
per = int(input("Enter percentage: "))
h = float(input("Enter your height: "))
#print("My name is " + name + " and I scored " + str(per) + "%. My height is" + float(h)+".")


citi=bool(input("Are you indian citizen: "))
print(citi)
print(type(citi))
'''

'''
name=input("Enter your name:")
print(name)
print(type(name))


marks=input("Enter Your 10th Marks:")
num_marks=int(marks)#explicit TC /Parsing
print(num_marks+20)#int+int
print(type(marks))

num_marks=int(input("Enter Your 10th Marks:"))#Explicit Typecasting
print(num_marks+20)

height = float(input("Enter your height:"))
print(height+2.1)
'''
#ip=str(input("Enter Your Ip:"))
#print("This is you Ip:", ip)

'''
ip2=str(input("Enter your Ip:"))
print(f"This is your ip:{ip2}")
print(type(ip2))

l = [20, 30 , 50 , 60]
print(type(l))
t = (20, 30 , 40 ,50)
print(type(t))
s = {20, 30 ,30 ,40}
print(type(s))
d = {"1" : 20, 2 :  30, 3 : 40}
print(type(d))
st="Hello" 'hello' "HELLO"
print(type(st))
'''
'''
iscitizen = input("Are u indian:")
print(iscitizen)
print(type(iscitizen))

iscitizen = bool(input("Are u indian:"))
print(iscitizen)
print(type(iscitizen))
'''


