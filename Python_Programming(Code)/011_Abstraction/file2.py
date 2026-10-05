from abc import ABC, abstractmethod
class Minister(ABC):
    @abstractmethod
    def create_awareness(self):
        pass

    def Publish_report(self):
        print("Quarterly reports shud be submitted")

class Health_Minister(Minister):
    def create_awareness(self):
         print("Conduct vaccination drives")

M1=Health_Minister()
M1.create_awareness()
M1.Publish_report()