'''

    -SYNTAX to create list comprehension:
            l1=[expression for variable in sequence]

    1.
        nl=[i+10 for i in [2,3,4,5,6]]
        print(nl) #output:[12,13,14,15,16]

        print(list(map(lambda i:i+10,[2,3,4,5,6])))

    2.
        nl=[i**3 for i in [2,3,4,5,6]]
        print(nl)


        ol=["Amy","Ben","Chad","Divya","Evan"]
        nl=[len(i) for i in ol]
        print(nl)

    -2nd SYNTAX to create list compreshension

        l2=
    ==============================================================================
    =
    ==============================================================================
    ==============================================================================
    =

ol={2:10,3:20,4:30,5:40,6:50}
print({i:(ol[i]**2 if i%2==0 else ol[i]**3) for i in ol})
            #OR     #using uppacking
print({k:(v**2 if k%2==0 else v**3) for k,v in ol.items()})

'''



