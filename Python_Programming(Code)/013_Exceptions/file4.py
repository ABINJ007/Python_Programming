class InValidAmountException(Exception):
    pass
class InSufficientBalance(Exception):
    pass

class BankAccount:
    def __init__(self, cname):
        self.cname = "ABC"
        self.balance = 50000
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
        else:
            raise InValidAmountException("Invalid Amount")
    def withdraw(self,amount):
        if amount<= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount} from account. New balance is {self.balance}")
        else:
            raise InSufficientBalance("Insufficient Balance")

ba = BankAccount("ABC")
try:
    ba.deposit(-5000)
    ba.withdraw(500)
except (InValidAmountException,InSufficientBalanceException)as e:
    print(f"Exception Handled: {e}")

print("END")


        