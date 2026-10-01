'''
Encapsulation:

->The process of protecting data by making the variable private and controlling
their access through public setter and getter methods
or
bundling/wrapping data and methods together and protecting data from outside access
->Direct access IS NOT given to sensitive data, BUT the class shud control How
the data is read/modified

Steps to achieve Encapsulation:
1)A class should be public non abstract class
2)define  private variables
3)Have public setter method(to update the data with validation logic
4)Have public getter method(to access / read data safely

    Note:
    Setter method:
    -used to modify private data
    - usually expected to take 1 Paramete
    - validation logiv should be present inside it
    - not supposed to return any value

    getter method:
    -used to access private data
    - usually does not take parameter
    - supposed to return any value


    Syntax:
        class ClassName:
            def __init__(self):
                self.__var=None #privateIV

            def set_var(self,newvalue): # Publicsettermethod to modify private
                #validation logic                variable upon validation
                self.__var=newvalue

            def get_var(self):  #publicgettermethod to read/Access private variable
                return self.__var
        obj=ClassName()
        obj.set_var(newvalue) #calling settermethod
        print(obj.get_var())  #calling gettermethod


    Achieving Encapsulation using @ Property decorator property decorator in python is
    a way to access methods like variables

    - There are 2 Decorators
    1)@property
    2)@<property > .setter

    1)Is a decorator, allows method to behave like "getter"
    -> instead of calling it normally like a method, we can ACCESS it like
    a normal attribute
    ex:
    print(instanceref.variable)

    2)Is a decorator defines the "setter" for the same property
    -> allows you to ASSIGN a value like a variable, but indirectly it calls
    a method
    ex:
    instanceref.variable= newvalue

Syntax:

class ClassName:
    def __init__(self):
        self.__var=None #private IV

    @property
    def var(self): #getter method
        return self.__var #access private IV inside class
    @var.setter
    def var(self,new_value): #setter method
        #validation Logic
        self.__var=new_value #access private IV inside class

    obj= ClassName()
    print(obj.var)  # getter method gets calles if u access it like a variable
    obj.var = value  # setter method gets called if u access it like a variable

    1)Getter MUST come first(becoz getter defines the property
    2)Setter MUST come after the Getter(setter works on that property)
    3)Always use same method name for both setter and getter and the property


    Advantages of using Property:
    1)it gives you attribute access with method control
    2)looks like attributes but works like a method.
    3)when requirements change, the code does not break

== ================================================================================
'''
