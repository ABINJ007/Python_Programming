'''
class Noodles:
    def use_fork(self):
        print("Noodles ara generally eaten using fork")

class Chineese_Noodles(Noodles):
    def use_chopstick(self):
        print("Chinese Noodles are generally eaten using chopstick")

cn=Chineese_Noodles()
cn.use_fork()
cn.use_chopstick()
'''

class Noodles:
    def consume(self):
        print("Noodles ara generally eaten using fork")


class Chineese_Noodles(Noodles):
    def consume(self):
        print("Chinese Noodles are generally eaten using chopstick")


cn = Chineese_Noodles()

cn.consume()
print(Chineese_Noodles.__mro__)

