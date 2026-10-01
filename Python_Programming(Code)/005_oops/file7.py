class Employee:
    def __init__(self):  # initializer executes each time instance is created
        print(self)


e1 = Employee()
print(e1)  # value


class Pen:
    def __init__(self, a, b, c):  # initializer executes each time instance is created
        self.cost = a
        self.height = b
        self.quantity = c

        # |      |     |--------------parametername
        # |      |----------IVname
        # ---Current object
print(Pen.__dict__)

p1 = Pen(10, 20, 30)
print(p1.__dict__)
p2 = Pen(40, 50, 60)
print(p2.__dict__)
p3 = Pen(70, 80, 90)
print(p3.__dict__)


class Employee1:
    def __init__(self, name, eid, salary):  # initializer executes each time instance is created
        self.name = name
        self.eid = eid
        self.salary = salary
        # |      |     |--------------parametername
        # |      |----------IVname
        # ---Current object


e1 = Employee("Girish", 21, 4000)
print(e1.__dict__)
e1 = Employee("Ramesh", 29, 44000)
print(e1.__dict__)
e1 = Employee("Suresh", 27, 45000)
print(e1.__dict__)

print(Employee1.__dict__)
