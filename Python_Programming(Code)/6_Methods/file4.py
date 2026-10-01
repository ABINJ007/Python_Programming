class Student:
    @staticmethod
    def calculate_percentage(marks,total_marks):
        return (marks/total_marks)*100
print(Student.calculate_percentage(75,200))#access the SM using ClassName
s1=Student()
print(s1.calculate_percentage(515, 625))  # access the SM using object reference
