''' Dictionary
-----------
1)It is a pre-defined class in python
2)Dictionary Allows to store Data in the form of Key and Values
3)One Key Along with its value is known as one item, Therefore Dictionary is a collection of Items.(Key Value pairs)

syntax to create empty dict ---> variablename = {} or dict()
Syntax --->dictwith.key,value--> variablename = {key1: value1, Key2: value2, key3: value4,......}
                                                 ------------  ------------  -------------
                                                   item1          item2         item3 
'''
d1={}
print(type(d1))
print(d1)
d1={14:400}
print(type(d1))
print(d1)


d2 = {1:100, 2:200, 3:300}
print(type(d2))
print(d2)
'''
Features of Dictionary
----------------------
1) Dict is NOT index based, but it  is based on key.
2) Dict is Ordered Collection
3) Key--->Homogenous<-----Values
      |--->Heterogenous<---|
4) Keys cannot be duplicated
   values can be Duplicated
5) Dict is Mutable.

Stack Memory/Variable Space |Value Space/Heap Memory
---------------- ---------- |----------------------
                            |
                            |
                            |
                            |
                            |                      
'''
print(d2[3])#Dict is not indexed based.
#Syntax to Access a value of dict
#reference_var[key]

#Syntax to Modify a value of Dict
#reference_var[key]=new_value

d2[1]=900
print(d2)#update

#Methods of Dictionary:
#---------------------

d3={}
d3[29] = 200#Syntax to modify value or add key-value to Dict
d3[70] = 56
print(d3)

#1)ref.setdefault(key,Optionalvalue)
#it adds the  key with the given value into Dict , But the value is not give the defauld value Noe will Used.
d4={}
d4.setdefault(10,100)
d4.setdefault(20)
print(d4)

#2)ref.update(Dict)
#it copies and adds the items of dict into reference.
d3.update(d4)
print(d3)

#3)ref.get(key)
#it returns the value for the key , if the key is not present it returns None.__

print(d3.get(70))
print(d3.get(777))

#4)ref.pop(key)
#it removes the entire item and returns the value.
#if the key is not there, it gives KeyError.
d3.pop(29)
print(d3)

#5)ref.popitem()
#it will removes the last value.

d3.popitem()
print(d3)
'''
d5 = {}#it will gives a Key Error.
d5.popitem()
print(d5)
'''
#6)ref.clear()
#it clears the dict makes it empty
d3.clear()
print(d3)

#7)ref.keys()
#it returns a list of keys from the Dict.

d7 = {1:100, 2:200, 3:300}
print(d7.keys())

#8)ref.values()
#it returns the list of values from the Dict

print(d7.values())

#9)ref.items()
#it returns the list of items from the dict but in a tuple format.
print(d7.items())
   
#in Django,Fastapi,AIML,Json
