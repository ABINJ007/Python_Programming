'''
Generator:
----------
-Generator is a Function that is used to create a custom sequence of elements using the "yield" keyword.
-If a user-defined function contains at least one yield keyword, then that function becomes a generator function.
-Generators generate values one-by-one (not all at once).
-Generators are 'mainly used to create custom sequence (like even numbers, odd numbers, fibanacci, primes, infinte sequences,large data streams).

-Generators object is created ONLY ONCE, When the "Function containing YIELD keyword" is called.
-Each yield returns ONE value, when next() or for loop asks for it.
yield:
    when python executes yield:
1.It returns the yielded value to the called.
2.It "pauses" the function (remembers variables and the next line).
3.When you call next() again, it "resumes right after yield".
4.Automatically creates an iterator.


print("---------------------------------")


def fun():  # generator Function
    yield 10
    yield 20
    yield 30


# when generator function is called, generator object is returned.
gen_obj = fun()
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print("---------------------------------")


def fun():
    value = 0
    yield value

    value = value + 1
    yield value

    value = value + 2
    yield value**2

    value = value + 3
    yield value**3

    value = value - 2
    yield value**2


gen_obj = fun()


print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))


for i in gen_obj:
    print(i)



'''