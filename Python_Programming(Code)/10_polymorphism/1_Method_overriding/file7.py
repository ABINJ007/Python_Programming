class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

class Citizen(Person):
    def __init__(self, name, age, height, citizen_id, nation, country):
        super().__init__(name, age, height) #calling parent constructor from child constructor
        self.citizen_id = citizen_id
        self.nation = nation
        self.country = country

c=Citizen("John Doe", 30, 5.9, "123456789", "USA", "United States")
print(c.__dict__)
