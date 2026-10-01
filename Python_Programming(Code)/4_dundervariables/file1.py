print(type(__name__), __name__)
# If we execute a module containing __name__ directly using python -m package.module
# __name__=="__main__"
print(__name__ == "__main__")
# if we execute a module containing __name__ Indirectly as a result of import, __name__=="package.module"
print("___________________________________________")


def add(x, y):
    print(x+y)
# add(10,20)#test the code

if __name__ == "__main__":
    add(10, 20)

