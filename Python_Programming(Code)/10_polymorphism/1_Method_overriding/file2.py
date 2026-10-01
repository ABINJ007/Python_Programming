class Calculator:
    def add(self, a, b):
        print(a + b)

    def add(self, a, b, c):
        print(a + b + c)

    def add(self, a, b, c, d):
        print(a + b + c + d)  #--->All methods are store in class dictionary and the last method will override the previous methods. So, only the last method will be called.

c=Calculator()
c.add(1, 2, 4, 7)
#c.add(1, 2, 3)
#c.add(1, 2, 3, 4)   


class Calculator:
    def add(self, *args):
        print(args)  #--->This is called as method overloading. Here we can pass any number of arguments and it will calculate the sum of all the arguments.
c1=Calculator()
c1.add()
c1.add(40)
c1.add(50,60)
c1.add(70,60,70,10)


class Calculator:
    def add(self, a=10, b=20, c=30):
        print(a + b + c)


c1 = Calculator()
c1.add()
c1.add(40)
c1.add(50, 60)
c1.add(70, 80, 10)

