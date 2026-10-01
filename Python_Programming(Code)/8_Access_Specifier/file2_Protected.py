class BankAccount:
    bank_name = "SBI"  #publicCV
    _interest_rate=5   #protectedCV

    def __init__(self,cname,accno):
        self.cname=cname  #publicIV
        self._accno=accno #protectedIV

    def _calculate_interest(self,amount):  #protectedIM
        return (self._interest_rate*amount)/100         #Access protected CV inside protectedIM     (inside class)itself

class SavingsAccount(BankAccount):
    def show_interest(self,amount):
        print(self._calculate_interest(amount))#Access protected IM from the child class

s1=SavingsAccount("ABD",121932332)
s1.show_interest(500000)
print(s1._accno)   #Access Protected IV outside the class