class Employee:
    def work(self):
        print("work")
class FrontEndDev(Employee):
    def render(self):
        print("Render")
class BackEndDev(Employee):
    def Connect_db(self):
        print("Connect Database")
class FullStackDev(FrontEndDev, BackEndDev):
    def deploy(self):
        print("Deploy")

em=FullStackDev()
em.deploy()
em.Connect_db()
em.render()
em.work()
print(FullStackDev.__mro__)
