'''
Types of Error:
---------------
At a high level, errors can be broadly classified into two categories:
1)Syntax Errors
2)Runtime Errors

1)Syntax Errors ->Errors that occur by violating Python's syntax rules.
                ->Python cannot properly parse the program
                ->Programmer has to correct them and only then program execution
                  will be started

            Ex:
                name= Python
            Ex:if condition colon missing
            Ex:list(
2)Runtime Errors->Problems that occur while the program is executing and are
                  represented by python exception object/classes.
                ->End User Input
                ->Unavailable resources,
                ->Invalid operations, etc
            such types of errors are called exception.



NOTE:
"At a high level, we can think of errors as syntax problems and problems encountered
during execution. Python represents many of these runtime problems as execeptions,
and exceptions are organized in a class hierarchy."

--------------------------------------
Normal FOllow of Python execution:

In a program, if all the statements are executed as per the conditions successfully
and we get the output as expected. then its called Normal Flow of python execution.



ex:

print(1)
print(2)
print(3)
print(4)
print(5)


ABnormal Flow of Python Execution:

while executing the statements in a program , if any error occurs at RUNTIME, then
immediately the program flow gets TERMINATED abnormally, without EXECUTING "the
below lines of code".this is called as ABnormal Flow of Python execution.
ex:
print(1)
print(2)
print(hi)
print(4)
print(5)

---------------------------------------
Exception=>An unwanted/ unexpected event that disturbs the normal flow of program.
         ->Whenever an exception occurs, the programs terminates immediately and
           below lines won't execute and hence we need to Handle These exceptions
           on high priority.

'''