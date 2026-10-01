from typing import override
class SeniorStudent:
    def study(self):
        print("Student is studying.")

class JuniorStudent(SeniorStudent):
    @override
    def study(self):
        print("Students are studying in junior class.")

s=JuniorStudent()
s.study()


