from typing import override
class Student:
    def study(self):
        print("Student is studying.")


class MedicalStudent(Student):
    @override
    def study(self):
        super().study()
        print("Medical Students are studying.")
        super().study()
s = MedicalStudent()
s.study()
