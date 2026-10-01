from typing import override
class Person:
    def register(self,name):
        print("Person is registered.")
class Employee(Person):
    @override
    def register(self,name):
        super().register(name)
        print("Employee is registered.")
class Student(Person):
    @override
    def register(self,name):
        super().register(name)
        print("Student is registered.")

p = Person()
p.register("hello")
e = Employee()  
e.register("John")
s = Student()
s.register("Alice")