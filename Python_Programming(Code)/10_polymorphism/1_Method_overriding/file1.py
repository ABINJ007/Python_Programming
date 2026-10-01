from typing import override
class Chef:   #parent class
    def cook(self):
        print("Chef cooks food")
class ItalianChef(Chef): #child Class #step1) Inheritance
    @override
    def cook(self):                   #step2) Method name shud be same as parent method
        print("Italian Chef")         #step3) Implementation in child shud be different

chef=ItalianChef()#Instatiation
chef.cook()