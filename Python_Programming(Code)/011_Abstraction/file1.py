# from abc import ABC, abstractmethod
# class Shape(ABC):             #ABstract class is like contract
#     @abstractmethod
#     def find_area(self):
#         pass
# class Square(Shape):     #inheritance
#     def find_area(self): #method overriding
#         print("side*side gives Area of Square")

# sq=Square()
# sq.find_area()

from abc import ABC, abstractmethod

class Shape(ABC):#-------------------------------------------------------
    @abstractmethod                                                     #| 
    def find_area(self):#                                                |
        pass#                                                            |------Until the child class fulfils the contract
                                                                        #|     ->its instance cannot be created
class Square(Shape):  #subclass will also become abstract-----------------
    pass

sq = Square()

