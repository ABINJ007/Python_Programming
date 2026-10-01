class FootWear():
    def protect(self):
        print("Footwear")
class Shoe(FootWear):
    def durable(self):
        print("Shoe")
class SportShoe(Shoe):
    def custion_impact(self):
        print("Sport Shoe")

ss=SportShoe()
ss.durable()
