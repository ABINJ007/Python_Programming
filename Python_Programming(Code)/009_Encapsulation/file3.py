class Employee:
    def __init__(self):
        self.__salary = 0  # private IV

    @property
    def salary(self):  # public getter method
        return self.__salary  # access private IV inside class

    @salary.setter
    def salary(self, new_salary):  # public setter method
        if new_salary > 6000:  # VALIDATION LOGIC
            self.__salary = new_salary
        else:
            print("I will leave the job")
e=Employee()
print(e.salary)  # calling public getter method to access private value
e.salary = 100000  # calling public setter method to update private value
print(e.salary)  # calling public getter method to access private value