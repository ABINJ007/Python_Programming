'''
Copying in Python
1)General Copy
    - assigning one variable to another.
    -Both Variables refer to the same object in memory.
    -Changes made through one varible reflect in the other.

list1 = [10, 20, 30, [40, 50]]
list2 = list1
list1[2] = 200
print(list2)
list2[1] = 300
print(list1)




2)Shallow Copy:
    -creates a new container object, but copies only the references of elements inside it(not the nested ones).
    -Changes in nested elements still affect both copies.
'''
import copy
list1=[10,20,30,[40,50]]
list2=copy.copy(list1)
list2[2]=600
print(list1)
print("___________________________________")
print(list2)
print("___________________________________")
list1[3][0]=500
print(list1)
print(list2)
'''
3)Deep Copy:
------------
    -Creates a new container object and Recursively copies all nested objects too.
    -Changes in one do not affect the other.


'''