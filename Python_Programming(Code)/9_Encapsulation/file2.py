class BankAccount:
    def __init__(self, cname):
        self.cname = cname
        self.__balance = 1000

    def view_balance(self): #public IM getter method
        return self.__balance #access private variable

    def deposit(self,amount):#PUBLIC IM setter method
        if amount > 0:#VALIDATION LOGIC
            self.__balance=self.__balance+amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self,amount):#public IM setter method
        if amount>0 and amount<=self.__balance:
            self.__balance =self.__balance-amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

     

b1=BankAccount("Ambani")
print(b1.view_balance())
b1.deposit(79800)
b1.withdraw(60000)

print(b1.view_balance())

b1.deposit(-354435)
b1.withdraw(60000)

