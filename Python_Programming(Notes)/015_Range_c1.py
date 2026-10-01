'''
RANGE:
    -range is implemented as a class.
    -when you call range(), you are actually creating a range object(as instance
     of the range class).
    -its a immutble sequence type like tuple or string

    -Syntax:
        -range(stop)
        -range(start, stop)
        -range(start, stop, step)
                 ^      ^     ^
                 |      |     |
                D.V=0   NO   D.V=1

     -Usaage of range:
         -when needed a sequence of numbers (for counting,indexiong,interation).
          range() doesnt actually create all the numbers -it just remembers.
          how to generate them.
         -when you want to loop a specific number of times.
         -when you want to avoid creating large lists in memory.

     -features or range():
         -immutable->once created, it cannot be changed.
         -lazy/memory-efficient->doesnt generated all numbers at once.
          it stores only:
              -start
              -stop
              -step
          and generated numbers when needed on demand.
         -iterable->can be used in for loops.
         -supports indexing and slicing.

     

r=range(1,8,1)
print((r),type(r))

#explicit typecasting on range object
print(list(r))
print(tuple(r))

r=range(11,45,11)
print(list(r))

#print first 11 natural numbers starting from 1
r=range(1,12)
print(tuple(r))


#generate neg numbers using range
print(list(range(-9,2,2)))
'''







