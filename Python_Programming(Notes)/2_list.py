l=[]
#ref.append(object)
#it append the object to the end of the list

l.append(10)

l.append(20)
l.append(30)

print(l)



#Insert
#Ref.insert(insert, object)
#it insert the object into specifid index

l.insert(2, 85)
print(l)

#ref.extend(collection)
#it copies and appends the collection elements into the list
l2=[11,12,33]
l.extend(l2)
print(l)
print("--------------")
l4=[10,20,30]
l5=[11,22,33]
l6=l4+l5#new list is created
print(l6)


#ref.pop()
#it removes and returns the last elements from the list
#ref.pop(index)
#it returns and removes the specific index elemets from the list
l6.pop()
print(l6)

l6.pop(2)
print(l6)

#ref.remove(object)
#it removes the specify object from the list and it removes first occuring obj

l7=[10,20,10,30,10,40]
l7.remove(10)
print(l7)

#ref.clear()
#it removes entire list elements
l7.clear()
print(l7)

#ref.count(obj)
#it returns the number of occurances of that obj
l8=[22,13,34,11,45,11]
number=l8.count(11)
print(number)

print("-----")
#ref.index(obj)
#it returns the index ni=umber of the 1st occuring obj
l8.index(11)
print(l8.index(11))

print("---------")
#ref.sort()
#it sortd in accendiing order
l8.sort()
print(l8)

print("-----")
#ref.reverse()
#it reverses the list
l8.reverse()
print(l8)

