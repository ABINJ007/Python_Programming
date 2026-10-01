'''
Dunder variables -> predefined sqecial varibles with double underscores at the start and end
            ->created automatically by python.
applications/use of dunder varibles
    1)identifying modules
    2)track where file are stored
    3)provide documentation
    4)controls how models will behave when they are imported.

    __name__
    __file__
    __cached__
    __package__
    __doc__

    1)__name__
            -> it provides name of the module
            -> if module is Directly executed or if that module executed as result of importing, __name__ gets initialised.
            -.If the moduel is executed directly= >__name__ will be set to 'main'
            -> If the modulue iis executed as result of Importing = >__name will be set to actul module name

      Note: To prevent Certain code from executing whenever a module is imported, that certain code should be places inside a conditional block
              if __name__=='__main__':
                  #test code

    2)__files__ => it shows the ful path of that module/file, which is currently being executed at the moment

    3)__package__=>it is used by import system which tells to which package  the module belongs to

                 =>gives the package  name of currently executing module

    4)__cashed__=>it stores the full file path of the bytecode generated for that module

    5)__doc__=>it stores the doc string of module, class, function
             =>doc string=>string written at very begining of a module, or class, or function,or method
             =>used for documentation purpose and to tell the purpose of that code
'''