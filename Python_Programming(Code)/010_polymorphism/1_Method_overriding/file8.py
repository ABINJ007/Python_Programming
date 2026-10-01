class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
class Citizen(Person):
    def __init__(self, name, age, height, citizen_id, nation, currency):
        super().__init__(name, age, height) #calling parent constructor from child constructor
        self.citizen_id = citizen_id
        self.nation = nation
        self.currency = currency

class Refugee(Citizen):
    def __init__(self, name, age, height, refugee_id, origin, exitdate):
        super().__init__(name, age, height, refugee_id, origin, exitdate) #calling parent constructor from child constructor
        self.refugee_id = refugee_id
        self.origin = origin
        self.exitdate = exitdate    


        