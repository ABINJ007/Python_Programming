'''
Set:
---
Set is a predefined class in python.
Syntax to create empty set--> variblename = set()

Syntax ---> set with elements --> variblename = {v1, v2, v3, ......}

'''
s1=set()
print(s1)
print(type(s1))

s2 = {10, 20 , 30 ,40 }
print(s2)
print(type(s2))

'''
Features of set
---------------
1) Set is not index based. (no pos indexing, neg indexing)
2) Unordered Collection.( Sequence of Not Retained)
3) Set Allows Both Homogenous & Heterogenous D.t/Elements.
4) Set Does Not allows Duplicates.
5) Set is Mutable.


Memory allocation:

'''

#s2[3]
s2 = {10, 20.1, 30j,True, 50}
print(s2)
print(type(s2))
#----------------------------------------------------------------------------
print("---------------------------------------------------------------------")
'''
Methods of Set:  (update the set values using Method)
--------------

'''

s1 = set() # empty set

#1)ref.add(object)
#it adds the object randomly into the set.
s1.add(25)
print(s1)
s1.add(26)
s1.add(27)
s1.add(28)
print(s1)


#2)ref.update(Collection)
#it copies and add the collection element into the the refset.

s2 ={ 10, 20 , 30 }
s1.update(s2)
print(s1)

s1.add(5)
print(s1)

#3)ref.pop()
#it removes an arbitary(Random) element from set.

s1.pop()
print(s1)

#4)ref.remove(object)
#it removes the specified object from the set.

s1.remove(25) #it takes a parameter
print(s1)
#if the object is not present, will get and keyerror.

#5)ref.discard(object)
#it removes the specified object from the set.
#if the object is not present, It DOES NOT raise error

s1.discard(24)
print(s1)

#6)ref.clear()
#it removes all the set elements

s1.clear()
print(s1)

#7)ref.issubset(set2) -->it takes another set
#it checks if set2 contains all the elements of set1 and returns boolean value.
s3 = {10, 20, 30}
s4 = {20, 30 , 10 , 40}
print(s3.issubset(s4))#True

s3 = {10, 100}
s4 = {20, 30 , 10 , 40}
print(s3.issubset(s4))#False

s3 = {10, 20, 30}
s4 = {20, 30 , 10 , 40}


print(s4.issubset(s3))#False
#8)set1.issuperset(set2)
#it checks if set1 contains all the elements of  set2 and returns boolean value.

print(s4.issuperset(s3))#True

#9) set1.isdisjoint(set2)
#it returns False if there is Atleast 1 common elements b/w both set
print(s3.isdisjoint(s4))#False 

#10)set1.union(set2)
#it returns a new set which contains unique elements of both sets.
s5={11, 23, 33}
s6 = {33, 44, 55}
print(s5.union(s6))

#11)set1.intersection(sets)
#it return a new set which contains common elements of both sets.

print(s5.intersection(s6))

#12)set1.symmetric_difference(set2)
#it returns a new set which contains uncommon of both sets.
print(s5.symmetric_difference(s6))


#13)set1.difference(set2)
#it returns a new set which contains elements of set1 but not present in set2
print(s5.  difference(s6))


