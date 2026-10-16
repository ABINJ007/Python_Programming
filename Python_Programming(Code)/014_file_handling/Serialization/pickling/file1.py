import pickle
class Student:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

with open("014_file_handling/Serialization/pickling/pickled_data.pkl","w+b") as f:
    s = Student("Akash", 20)
    bin_data=pickle.dump(s,f)
    f.write(bin_data)
    

    