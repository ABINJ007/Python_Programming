class Book:
    def __init__(self, name, author):
        self.namel=name
        self.author=author

    def __repr__(self):#method overriding
            return "repr custom string"

b1=Book("Maths","Daniel")
print(b1)
print(repr(b1))