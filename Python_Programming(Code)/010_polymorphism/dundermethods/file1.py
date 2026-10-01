class Pen(object):
    def __init__(self):
        print("initializer")

#P=Pen()
p=Pen.__new__(Pen)#step 1 (new pen created and returned)
Pen.__init__(p)#step 2 (initializer code)