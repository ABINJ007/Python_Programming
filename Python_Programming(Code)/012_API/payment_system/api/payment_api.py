from abc import ABC, abstractmethod
class PaymentAPI(ABC):
    @abstractmethod
    def authenticate(self):
        pass
    @abstractmethod
    def pay(self,amount):
        pass
    