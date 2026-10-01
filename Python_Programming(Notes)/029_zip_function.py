'''
zip function:
------------
    -It is a predefined function in python that combines multiple iterables element. by element
    -It creates tuples of corresponding elements from each iterable.
    -Zip Function Accepts two or more iterables and "returns" Zip object "Iterator"

    Syntax:
        zip_obj = zip(iterable1, iterable2, .....)

    Note: Each element inside zipobject is a tuple
       ->zip stops at the shortest iterable
       ->it is used for mapping & pairing


       
rolls = [32,40,60,33]
names = ["Amy","Ben","Chad","Denzo"]

print(list(zip(rolls,names)))

rolls1 =[2,3,4,5,6]
marks =[30,65,90,50,25]


#print(zip(rolls1,names)){rolls1:("Pass" if marks>35 else "Fail") for rolls1,names in items()})
obj=zip(rolls1,marks)
print({k:("Pass" if v>35 else "Fail") for k,v in obj.items()})


'''
