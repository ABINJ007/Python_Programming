class Park:
    authority= "GBA" #Public    CV

    def __init__(self,name,location):
        self.name=name           #Public  IV
        self.location=location

    def open_park(self):#Public   IM
        print("Park opens on Weekdays",self.name)

    @classmethod
    def change_authority(cls,new_authority): #public
        cls.authority=new_authority # modify public CV inside the class

p1=Park("ABC","asdffggg")
p1.open_park()#Access the public IM outside the calss