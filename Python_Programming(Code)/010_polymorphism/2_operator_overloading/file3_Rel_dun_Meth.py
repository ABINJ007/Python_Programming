class Money:
    def __init__(self, value):
        self.value = value
    def __lt__(self,other):
        return self.value<other.value
    def __eq__(self,other):
            return self.value==other.value
    def __ne__(self,other):
            return self.value!=other.value
    def __le__(self,other):
            return self.value<=other.value
    def __ge__(self,other):
            return self.value>=other.value
    def __gt__(self,other):
            return self.value<other.value
            def __lt__(self,other):
                    return self.value<other.value







m1=Money(100)
m2=Money(200)

print(m1<m2)
print(m1!=m2)