class Batsman():
    def bat(self):
        print("Batsman")
class Bowler():
    def bowl(self):
        print("Bowler")
class AllRounder(Batsman, Bowler):
    def field(self):
        print("Fielder")

cr=AllRounder()
cr.bat()
cr.bowl()
cr.field()
print(AllRounder.__mro__)
