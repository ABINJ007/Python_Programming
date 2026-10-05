from payment_method.credit_card import CreditCard
from payment_method.upi import UPI

class OnlineStore:
    def __init__(self,paymentmethod):
        self.paymentmethod=paymentmethod

    def process(self,amount):
        print("Processing Transcation")
        self.paymentmethod.authenticate()
        self.paymentmethod.pay(amount)
        print("Successful Transaction")

payment1=CreditCard()
payment2=UPI()



order1=OnlineStore(payment1)
order1.process(50000)