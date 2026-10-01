'''
String
------
it is a pre-defined class in Python.
String is collection/Sequence of character, enclosed within pair of '',"", ''' '''.
Character includes uppercase letters, lowercase letters, Digits, spaces, Special Characters all the thing can be added.
'''
s='HELLO',"hello",'''Hello'''
print(s)
print(type(s))
s1='hello'
print(type(s1))

s2=str()#4th way to define a emptystr
print(s2)
print(type(s2))
'''

1)string is an index Based Collection.(pos,neg indexing).
2)String is an Ordered Collection.
3)String is Immutable

Stack Memory/Variable Space |Value Space/Heap Memory
---------------- ---------- |----------------------
         -----   ---------->|'p''y''t''h''o''n'
        | 0x1 |             | 0  1  2  4  5  6
         -----              |
           S                |
'''
s1="who am i"
#varible= len(Collection)#it is a pre-defined Function in Python.
#It return the no of elements present in the collection.

#Methods of String

#1)ref.capitalize()
#it Returns a copy of a String Where only the 1st letter will be Capitalize
print(s1.capitalize())

#2)ref.title()
#it returns copy of a string where 1st letter of each word is Capitalize.
print(s1.title())

#3)ref.upper()
#it returns a copy of string which is in uppercased form.
print(s1.upper())

#4)ref.lower()
#it returns a copy of string which is in Lowercased form.
print(s1.lower())

#5)ref.isupper()
#it returns True id the String is an uppercase String.
print(s1.isupper())

#6)ref.islower()
#it returns True id the String is an lowercase String.
print(s1.islower())

#7)ref.startswith("substring")
#it return True if the string startswith the given substring
s2="Cherry Cheriyan"
print(s2.startswith("Cherry"))

#8)ref.endswith("substring")
#it returns True if the string endswith the given substring.
print(s2.endswith("yan"))

#9)ref.replace("oldstring", "newsubstring")

print(s2.replace("Che", "riya"))

#10)ref.isalpha()
#if returns True if string contains only alphabets(upper or lowercase).

s3="CHERIYAN 2.O"
print(s3.isalpha())

#10)ref.isdigit()
#if returns True if string contains only digit.
s3="9443197656"
print(s3.isdigit())

#11)ref.isalnum()
#it returns True if string contains either alphabets or digits or both.

s4="CHERIYAN2O"
print(s4.isalnum())

#12)red.swapcase()
#it returns a copy of string where upperletter are swapped with lowercase and vice versa.
s5="CHErIYAn"
print(s5.swapcase())

#13)ref.count("substring")
#it returns the number of occurances of the substring.
s7="CHERICHERI"
print(s7.count("CHERI"))

#14)ref.index("substring")
#It returns the index number of the 1st substring.
s8="prestige"
print(s8.index("e"))

#16) ref.lstrip()
#it returns the copy of a string with leading/left-hand-side spaces removed
s9="  BOOM"
print(s9.lstrip())

#17) ref.rstrip()
#it returns the copy of a string with trailing/right-hand-side spaces removed
s10="BOOM  "
print(s9.rstrip())

#18)ref.strip()
#it returns a copy of string with both leading & Trailing spaces remove.
s11=" SUPER CUP "
print(s11.strip())

#19)ref.split()
#it splits the string based on space as separator and returns list of substrings
s12="dhee coding lab"
print(s12.split())


#20)"substring".join(listofstrings)   
#it returns a copy of a string with the substring joined b/w those strings

dates=["15","08","1947"]

#15/08/1947
print("/".join(dates))

s=" Today is Friday Good Afternoon "
print(len(s.split()))
s1=s.split()
print(s1[2])

















    



         




















                            















