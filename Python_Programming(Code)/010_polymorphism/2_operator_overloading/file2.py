class Money:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Money(self.value + other.value)
    

    def __sub__(self, other):
            return Money(self.value - other.value)
    def __mul__(self, other):
            return Money(self.value * other.value)
    def __truediv__(self, other):
            return Money(self.value / other.value)
    def __floordiv__(self, other):
            return Money(self.value // other.value)
    def __mod__(self, other):
            return Money(self.value % other.value)
    def __pow__(self, other):
            return Money(self.value ** other.value)
    def __str__(self):
        return f"${self.value}"


m1 = Money(100)
m2 = Money(200)
m3 = Money(300)
m4 = Money(400)

print(m1 + m2)  # This will call the __add__ method of Money class #print(m1.__add__(m2))
print(m1 + m3)  # This will call the __add__ method of Money class #print(m1.__add__(m3))
print(m1 + m2 + m3)  # This will call the __add__ method of Money class #print(m1.__add__(m2).__add__(m3))
print(m1 + m2 + m3 + m4)  # This will call the __add__ method of Money class #print(m1.__add__(m2).__add__(m3).__add__(m4))

print(m1 - m2)  # This will call the __sub__ method of Money class
print(m1 * m2)  # This will call the __mul__ method of Money    
print(m1 / m2)  # This will call the __truediv__ method of Money
print(m1 // m2)  # This will call the __floordiv__ method of Money
print(m1 % m2)  # This will call the __mod__ method of Money
print(m1 ** m2)  # This will call the __pow__ method of Money

