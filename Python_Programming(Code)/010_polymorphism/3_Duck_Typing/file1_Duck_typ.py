class Zomato:
    def deliver(self):
        print("Zomato is delivering food.")

class Swiggy:
    def deliver(self):
        print("Swiggy is delivering food.")

class Swish:
    def deliver(self):
        print("Swish is delivering food.")
class Rapido:
    def commute(self):
        print("Rapido is used for commuting")

def process_delivery(partner):
    if hasattr(partner,"deliver"):   #<-------Safe Ducktyping
        partner.deliver()


r=Rapido()
z=Zomato()
s=Swiggy()
sh=Swish()

l=[z,s,sh,r]
for p in l:
    process_delivery(p)
print(hasattr(z,"commute"))