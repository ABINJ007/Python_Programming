class Product:
    def __init__(self, pid, name, price):
        self.pid = pid  #IV1
        self.name = name  # IV2
        self.price = price  # IV3

        def __hash__(self):
            return self.pid  #hash value of the object is based on pid
          



p1=Product(101,"Laptop",50000)
print(hash(p1)) #hash value of the object
p2=Product(102,"Mobile",20000)
print(hash(p2)) #hash value of the object

