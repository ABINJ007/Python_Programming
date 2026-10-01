class state:
    def __init__(self, state, Language, Capital):
        self.state=state
        self.Language=Language
        self.Capital=Capital
        
st1=state("Kerala","Malayalam","Trivandrum")
print(st1.__dict__)

st1.state = "Keralam"
print(st1.__dict__)