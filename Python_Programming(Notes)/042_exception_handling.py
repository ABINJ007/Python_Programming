'''
Exception Handling:
------------------
It Does Not mean reparing or correcting the exception, INSTEAD it is a process in
WHICH we Define a WAY, so that the program DOES NOT Terminate abnormally due to
exceptions.

->Highly recommended to handle Exceptions
->Main  objective of Exception Handling is Graceful Termination/Normal Termination
  of Application (ie, we shud not Block our resources and we should NOT miss anything)

----------------------------------------------------------------
Exception Handling in python is achieved -> using try and except blocks

syntax:
try:
    #code which may raise an exception
except ExceptionName:
    #execution handling code

->try block   ->try is a keyword in python
              ->the code which may raise an exception should be written inside the
                try block

->except block ->except is a keyword
               ->The corresponding Handling code for the exception, is occured needs
                 to be written inside the except block

-------------------------------
Exception hierarchy!!


DEFAULT Exception handling:
---------------------------
    In python, for every exception type, a corresponding class is available and
every exception is an object, so whenever an exception occurs -> PVM will create the
corresponding exception object and WILL CHECK FOR THE HANDLING code!

    If the particular HANDLING CODE is NOT available, then python interpreter
terminates the program abnormally, and prints corresponding exception information
to the console.

--------------------------
case1:
working=>1)If the code written in the try block raises an exception, only then the 4   
         execution flow goes to the except block for handling code.

         2)If there is NO exception raised by the code in the try block, Then the
         execution flow WON't go to the except block
----------------------------------------
case2:
        Exception shud occur only in try block only the code inside the try block
will be checked for the exception and its handling code. But, if there is any
exception for the code before the try block, then abnormal termination
------------------------------------------
case3:
        When no specific exception name is handled in except block, abnormal
termination occurs.
--------------------------------------------
case4:
        Skipping beloe lines inside try block

        If there are 3 lines of code inside the try block and an exception is
        raised the executing the first line, then the execution flow goes to the
        except block "without executing the remaining two lines".
----------------------------------------------
case5:
        What if execption occurs at except block itself, abnormal termination

        If an execption is raised inside the try block, the execution goes to the
        except block. if the code inside the expcept block also raises an exception
        then it leads to abnormal termination.




 '''