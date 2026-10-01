'''
print_funtion:
    -it is a predefined funtion in python which is used to display output on
     the console or the screen.
    -it helps the programmer see the result of program/code execution.

Print_funtion aas two default arguments:
    1.sep:
        -syntax:
            print(v1,v2,v3,sep=' ')
        -whenever multiple values are to be printed ussing prnt funtion,
         the value of the seperator will be printed in between those values
        -the default value of seperator(sep) is space(" ").
        -if there are n values to be printed the seperator(sep) value will be printed
         n-1 times in between them.
         
    2.end:
        -syntax:
            print(v1,v2,v3,end='\n')
        -when multiple values or single values is printed using print funtion
         at the end the value of the end argument will be executed or printed.
        -default value of end is "\n".
        -if there are n values to be printed the end argument value wil be
         printed only "once" at the end.
'''


#1. sep=" "

print(10,40,70,30,50,20)

print(10,40,70,30,50,20,sep="@")

print(10,40,70,30,50,20,sep="\n")

print("------------------")

#2. end

print(10)
print(20)

print(11,22,33,sep=" ",end="@")
print(44,end=" ")
print(55,66,sep="\n")
print("----------------------")

print(10,20,30,sep='\n',end=" ")
print(40,sep="",end="@")
print(50,60,70,sep="\n",end="\n")
print("stop")










