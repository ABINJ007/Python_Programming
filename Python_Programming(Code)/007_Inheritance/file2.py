class Employee:
    def work(self):
        print("work")


class Developer(Employee):
    def code(self):
        print("write the code")

D=Developer()#object creation
D.code()
D.work()
D.test()
print(Developer.__mro__)  # (<class '__main__.Developer'>, <class '__main__.Employee'>, <class 'object'>) Order in which search