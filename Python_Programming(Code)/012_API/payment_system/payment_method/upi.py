from api.payment_api import PaymentAPI
from random import randint


class UPI(PaymentAPI):
    def authenticate(self):
        pin = randint(1000, 9999)
        print(f"UPI Pin {pin} verified")
        print("UPI Authentication Done")

    def pay(self, amount):
        transc_id = randint(10000, 99999)
        print(f"Transaction id is {transc_id}")
        print(f"Paid {amount} using UPI")
