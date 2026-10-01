
'''
class Pen(object):
    def __init__(self):
        print("initializer")


# P=Pen()
p =Pen()  # step 1 
#print(p)
print(p.__str__())
'''
class Pen:
    def __init__(self,color,cost,brand):
        self.color=color
        self.cost=cost
        self.brand=brand
        print("initializer")
    def __str__(self): #step2
        return f"{self.color}->{self.cost}->{self.brand}" #step3
p1=Pen("red",20,"Camlin")
p2 = Pen("red",20,"Camlin")

print(p1)
print(p2)