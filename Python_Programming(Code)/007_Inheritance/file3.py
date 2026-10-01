class Phone():
    def call(self):
        print("call")
class MobilePhone(Phone):
    def send_sms(self):
        print("send SMS")
class SmartPhone(MobilePhone):
    def browse(self):
        print("browse")

sp=SmartPhone()
sp.browse()
sp.send_sms()
sp.call()