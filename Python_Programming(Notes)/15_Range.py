'''
Range:
----- - -> Range is implemented as a class .
      - -> When you call range(), you're actully creating a range object (an instance of the range class).
      -->it's an immutable sequence type like tuple or string
      syntax:
              -range(stop)
              -range(start, stop)
              -range(start, stop, step)
                       |      |     |
                      DV=0   none   DV=1(Default value)
Usage of range():
        ->when you need a sequence of numbers(for countin, indexing, iteration).range() doesn't actually create all the numbers - it just remembers how to generate them.
        ->when you want to loop a specific number of times
        ->when you wnat to avoid creating large lists in memory.

Features of range:
    1)Immutable --> once created, it cannot be changes.
    2)Lazy/Memory Efficient -->Doesn't generate all numbers at once. It stores only :
                -start
                -stop
                -step
        and generates numbers when needed on demand.
    3)Iterate -> Can be used in for loops.
    4)Supports indexing  & slicing.


result=range(1, 8, 1)
print(result)
print(type(result))

#Explicit typecasting on range object
print(list(result))
print(tuple(result))
print(set(result))
print(str(result))

result1=range(11, 46, 11)
print(list(result1))

result2=range(1, 12)
print(tuple(result2))

result3=range(-1, -10 , -2)
print(list(result3))

print(list(range(-9, 2, 2)))
'''