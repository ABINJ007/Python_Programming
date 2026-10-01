#tuple

#it is a predefined class in python

'''Features of tuple
-----------------
Is index Based collection

Ordered collection(Sequence is maintained)

Supports Both Homogeneous & Heterogeous

Allows Dupilates

Immutable collection(cannot add,remove,update a tuple)'''


 #tuple
#it iss a predefined class in python
#
t1=()
type(t1)
print(type(t1))

t2=tuple()
print(type(t2))

t3=(10,23,45,65)
print(type(t3))

t4=(98)#if i want a single tuple element then comma need ti be placed after the element
print(type(t4))
print(t3[2])
print( t3[-2])

#ref.count(object)
t3.count(23)
print(t3.count(23))

#ref.index(object)
ind=t3.index(45)
print(ind)



