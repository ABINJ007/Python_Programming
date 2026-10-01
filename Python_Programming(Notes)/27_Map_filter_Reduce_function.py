
'''
1) Map Function:
    -predefined HOF
    -Applies a given function to each item in iterable.
    -Returns a map object (an iterator).
    -"Used for applying common transformation logic to each else of iterable"
    syntax:
        map(function, iterable)
            -function ->shud takes one argument and return on value
            -iterable ->sequence (list, tuple , etc).

'''

from functools import reduce


def check_even(n):
    return n % 2 == 0


lst = []


def segregate(fun, col):
    for i in col:
        if fun(i):
            lst.append(i)
    return lst


l = [3, 8, 12, 13, 19, 22]
print(segregate(check_even, l))


print(list(map(lambda n: n % 2 == 0, [3, 8, 12, 13, 19, 22])))
'''
2)Filter Function:
    -filter out elements from an iterable based on a condition.
    -returns a filter object(an iterator)
    -filters only those elements wher the function returns True and adds it into filter object.
    Syntax:
        filter(function, iterable)
            -function -> thish function passed as a parameter must take 1 parameter and must return True or False.
            -iterable -> sequence

'''
print(list(filter(lambda n: n % 2 == 0, [3, 8, 12, 13, 19, 22])))

'''
l=["lathik","YASHAS","Sagar","RAJ","SAI","cherian"]
'''

print(list(filter(lambda n: n.islower(), [
      "lathik", "YASHAS", "Sagar", "RAJ", "SAI", "cherian"])))

print(list(map(lambda n: len(n), [
      "lathik", "YASHAS", "Sagar", "RAJ", "SAI", "cherian"])))

print(
    list((lambda n: len(n), ["lathik", "YASHAS", "Sagar", "RAJ", "SAI", "cherian"])))


def add(a, b):
    return a + b


def compress(fun, col):
    result = 0
    for i in col:
        result = result+i
    return result


l = [10, 20, 30, 40, 50]
print(compress(add, l))


def compress(fun, col):
    result = 0
    for i in col:
        result = fun(result, i)
    return result


l = [10, 20, 30, 40, 50]
print(compress(add, l))


def compress(fun, col):
    result = 0
    for i in col:
        result = fun(result, i)
    return result


l = [10, 20, 30, 40, 50]
print(compress(lambda a, b: a+b, l))

'''
3) Reduce Function
    -It's a function from functools module (from functools import reduce).
    -It applies a function "cumulatively" to the items of an iterable, reducing them to single value.
    Syntax:
        from functools import reduce
        reduce(function, iterable)

        function ->  a function that takes two arguments and shud return a Singlevalue
                    -takes two arguments
                    -returns one value
'''

print(reduce(lambda a, b: a+b, [10, 20, 30, 40, 50]))
print("++++++++++++++++++++++++++++++++++++")
print(reduce(lambda a, b: a*b, [10, 20, 30, 40, 50]))

l = [10, 15, 20, 25, 30, 35]
# lst=filter(lambda n:n%2==0,[10,15,20,25,30,35])
print(list(map(lambda j: j**2, filter(lambda n: n %
      2 == 0, [10, 15, 20, 25, 30, 35]))))
print(list(filter(lambda n: n % 2 == 0, [10, 15, 20, 25, 30, 35])))
