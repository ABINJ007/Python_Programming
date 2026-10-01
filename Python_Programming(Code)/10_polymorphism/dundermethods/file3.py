class Employee:
    def __init__(self,ENAME,EMP_ID,HIREDATE):
        self.ENAME=ENAME
        self.EMP_ID=EMP_ID
        self.HIREDATE=HIREDATE

    def __str__(self):
        return f"{self.ENAME}-->{self.EMP_ID}-->{self.HIREDATE}"

E1=Employee("ABC",123,'07-aug-26')
E2=Employee("CBA",456,'14-dec-24')

print(E1.__str__())
print(E1)
print(E2)