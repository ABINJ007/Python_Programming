class Student:
    def __init__(self,name,marks):
        self.name=name #publicIV
        self.__marks=marks #privateIV

    def parent_teacher_meet(self): #public IM
        print("Marks scored is:",self.__marks)#Accessing privateIV from inside class in public method




s1=Student("ABC",35)
print(s1.name)#Access public outside class
s1.parent_teacher_meet()
#print(s1.__marks)#NOt going to work(private) #Access privateIV outside the class