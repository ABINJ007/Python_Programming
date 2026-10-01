class Ornaments:
    def __init__(self,metal,price,grams):
        self.metal=metal
        self.price=price
        self.grams=grams
    def diplay_ornaments(self):#Access of IV's using IM
        print(self.metal)
        print(self.price)
        print(self.grams)
    def change_price(self,newprice):
        self.price=newprice
        print("price changed")

o1=Ornaments("Silver",7000,5)
o2=Ornaments("Gold",40000,10)
o3=Ornaments("Iron",500,1000)

o1.diplay_ornaments()
o2.diplay_ornaments()
o3.diplay_ornaments()
o1.change_price=70000
print(o1.change_price)