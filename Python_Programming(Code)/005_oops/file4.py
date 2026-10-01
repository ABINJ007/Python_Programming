class Student:
    pass
obj1=Student()#object1
obj2=Student()#object2
obj3=Student()

obj1.name="Cherian"
obj1.rollno=777 
obj1.email="cherian123@gmail.com"

obj2.name = "Daniel"
obj2.rollno = 108
obj2.email = "daniel123@gmail.com"
print(obj1.name,obj1.rollno,obj1.email)
print(obj1.__dict__)
print(obj2.__dict__)
#modiying
obj1.name="Daniel"
obj1.rollno=888
obj1.email="daniel123@gmail.com"
print(obj1.__dict__)
