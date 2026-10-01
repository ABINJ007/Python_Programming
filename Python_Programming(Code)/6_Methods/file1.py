class Student:
    school_name="ABC"
    principal="CBA"
    location="BCA"

    def __init__(self,name):
        self.name=name
    @classmethod
    def display_school_details(cls):
        print(cls.school_name)
        print(cls.principal)
        print(cls.location)
    @classmethod
    def change_principal(cls,newprinci):
        cls.principal = newprinci #Modification of CV Using cls
Student.display_school_details()
Student.change_principal("Cherian")
print(Student.principal)
    