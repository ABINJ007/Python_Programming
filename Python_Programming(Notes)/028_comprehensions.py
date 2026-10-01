'''
Comprehensions:
    -They  are python's way of writing loops that produce collections in a compact, readable form.
    -it combines => iteration+transformation+filtering


3 types of comprehensions:
--------------------------
    1)list comprehensions
        ->easier way to create lists (transformation+filtering)
    2)Set comprehensions
    3)dict comprehensions


    Syntax:(to create list comprehensions)
        l1 = [expression for variable in sequence] #iteration + transformation
'''
print("+++++++++++++++++")
ol = [2, 3, 4, 5, 6]

print([i+10 for i in [2, 3, 4, 5, 6]])

ol = ["Amy", "Ben", "Chad", "Divya", "Evan"]
# nl=[3,3,4,5,4]
print([len(i) for i in ["Amy", "Ben", "Chad", "Divya", "Evan"]])

'''                 (3)               (1)              (2)
    Syntax:    ----------  -----------------------  -----------
        #iteration+filtering+transformation+appending
        l2  = [expression for variable in sequence if condition]

'''
ol = [4, 7, 10, 13, 18]
# nl=[49,169]

print([i**2 for i in ol if i % 2 != 0])

ol = ["Amy", "Ben", "Chad", "Divya", "Evan"]
print([len(i) for i in ["Amy", "Ben", "Chad", "Divya", "Evan"] if len(i) > 3])

ol = ["Ms Amy", "Mr Ben", "Ms Chad", "Mr Divya", "Ms Evan"]
print([i for i in ["Ms Amy", "Mr Ben", "Mr Chad",
      "Mr Divya", "Ms Evan"] if i.startswith("Ms")])
print([i for i in ["Ms Amy", "Mr Ben", "Mr Chad", "Mr Divya", "Ms Evan"] if "Ms" in i])

'''
    Syntax:
        #iteration + filtering +Transformation + appending
        l3=[true_exp if condition else false_exp for variable in sequence]


'''
ol = [2, 3, 4, 5, 6, 7]
# nl = 4,27,16,125,36]

print([n**2 if n % 2 == 0 else n**3 for n in ol])
ol1 = ["Ms Amy", "Mr Ben", "Mr Chad", "Mr Divya", "Ms Evan"]
# nl = ["Beautiful", "Handsome", "Handsome", "Handsome", "Beautiful"]

print(["Handsome" if n.startswith("Mr") else "Beautiful" for n in ol1])


# nl = ["Beautiful Amy", "Handsome Ben", "Handsome Chad", "Handsome Divya", "Beautiful Evan"]
print(["Handsome"" "+n if n.startswith("Mr") else "Beautiful"" "+n for n in ol1])

'''
Set Comprehension
-----------------
1st syntax for Transformation only
s1 = {exp for var in collection}

2nd syntax for filtering only
s2 = {exp for varin collection if condition}

3rd syntax for Conditional transformation
s3={true_exp} if condition else false_exp for item in collection}

Dictionary Comprehension
-----------------
1st syntax for Transformation only general syntax
d1 = {key_exp: value_exp for item in iterable}
'''
l = [5, 7, 8, 10, 11]
# d={5:25.7:49,8:64,10:100,11:121}
print({i: i**2 for i in l})

l1 = [5, 7, 8, 10, 11]
# d={25: 125, 49: 343, 64: 512, 100: 1000, 121: 1331}
print({i**2: i**3 for i in l1})

Candidates = ["Amy", "Bennet", "Chadwick", "Divya", "EvanJovelin"]
# d1={'Amy': 3, 'Bennet': 6, 'Chadwick': 8, 'Divya': 5, 'EvanJovelin': 11}
print({i: len(i) for i in Candidates})

Candidates = ["Amy", "Bennet", "Chadwick", "Divya", "EvanJovelin"]
# d1={'Amy': 3, 'Bennet': 6, 'Chadwick': 8, 'Divya': 5, 'EvanJovelin': 11}

print({i: i[::-1] for i in Candidates})


'''
d2 = {key_exp : value:exp for item in iterable if condition)
                                                ------------
                                                   True
'''
l2 = [5, 7, 8, 10, 11]
print({i**2: i**3 for i in l if i % 2 != 0})


ol2 = ["Amy", "Ben", "Chad", "Divya", "Evan"]
ol2 = ["Ms Amy", "Mr Ben", "Mr Chad", "Mr Divya", "Ms Evan"]
print({i: "Handsome" for i in ol2 if i.startswith("Mr")})


'''
d3 = {key_exp :(True_exp if condition else False_exp ) for item in iterable}
                           ----------
'''
l4 = [4, 5, 6, 7, 8, 9]

print({i: (i**2 if i % 2 == 0 else i**3) for i in l4})

d1 = {2: 10, 3: 20, 4: 30, 5: 40, 6: 50}
print({i: (d1[i]**2 if i % 2 == 0 else d1[i]**3) for i in d1})

'''
d3 = {key_exp: (True_exp if condition else False_exp) for k, v in d1.items()}
# using unpacking
print({var1: (var2**2 if var1 % 2 == 0 else var2**3)
      for var1, var2 in d1.items()})

'''