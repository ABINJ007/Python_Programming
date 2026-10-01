class Student:
    def __init__(self, name):
        self.name = name  # public IV
        self.__marks = 0  # private IV

    def get_marks(self):  # public getter method
        return self.__marks  # access private IV inside class

    def update_marks(self, newmarks):
        if newmarks > 0 and newmarks < 101:  # VALIDATION LOGIC
            self.__marks = newmarks
            print("updated marks")
        else:
            print("invalid marks entered")


s1 = Student("amakfa")
print(s1.name)
print(s1.get_marks())  # calling publlic getter method to access private value

s1.update_marks(76)
