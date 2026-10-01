class Car:
    def __init__(self, modelno, price):
        self.modelno = modelno
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Car): #check if other is an instance of Car class
            return self.modelno == other.modelno and self.price == other.price #content comparison of two objects based on modelno and price
        else:
            return False #return False if other is not an instance of Car class



c1=Car(101,500000)
c2=Car(102,200000)
print(c1==c2) #print(obj1.__eq__(obj2)) #False because both are different objects