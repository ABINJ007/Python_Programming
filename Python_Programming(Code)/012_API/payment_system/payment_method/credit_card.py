from api.payment_api import PaymentAPI
from random import randint
class CreditCard(PaymentAPI):
    def authenticate(self):
        otp = randint(100, 999)
        print(f"Credit card otp {otp} verified")
        print("Creditcard Authentication Done")

    def pay(self,amount):
        transc_id = randint(10000, 99999)
        print(f"Transaction id is {transc_id}")
        print(f"Paid {amount} using Creditcard")

        