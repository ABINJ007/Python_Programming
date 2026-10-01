class Politician:
    def __init__(self,name,wealth):
        self.name=name                  #public IV
        self.__wealth=wealth            #private IV
    def __raise_funds(self):    #privateIm
         print("Politician raising funds")
    def ed_raid(self):
        self.__raise_funds()    #access private IM inside class within public method
        print(self.__wealth)    #access private IV insider class
        



p1=Politician("Trump",70000000)
#print(p1.wealth)
#p1.__raise_funds()
p1.ed_raid()