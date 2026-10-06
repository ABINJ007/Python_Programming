# print(1)
# print(2)
# print(hi)#code causing a issue/risky  #exception
# print(4)
# print(5)

print(1)
print(2)
try: 
    print(hi)
except NameError:
    print("Handled")
print(4)
print(5)
