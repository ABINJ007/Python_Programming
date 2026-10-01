class Bank:
    @staticmethod
    def calculate_interest(principle,roi,time):
        return (principle*roi*time)/100
Bank.calculate_interest(1000,7,2.5)
b1=Bank()
print(b1.calculate_interest(2000,7,4))