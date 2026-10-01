from typing import override
class WhatsApp1:
    def send_message(self):
        print("single Tick Supported")

class WhatsApp2(WhatsApp1):
    @override
    def send_message(self):
       super().send_message()
       print("Double tick Supported")

    def send_audio(self):
        print("audio Message sent")

class WhatsApp3(WhatsApp2):
    @override
    def send_message(self):
       super().send_message()
       print("Blue tick Supported")
    @override
    def send_audio(self):
        super().send_audio()
        print("Enhanced Audio Clarity Support")
    def send_video(self):
        print("Video format supported")
w=WhatsApp3()
w.send_message()
w.send_audio()