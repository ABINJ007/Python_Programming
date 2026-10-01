'''
concatanation:
-it means joining two or more string together to make one contious string.
-you can concatnation strings using the + operator

syntax:
    newstring="string1"+"string2"+...

'''
'''
player_name=input("Enter the player name: ")
age=int(input("Enter age: "))
average=float(input("Enter the batting average: "))
team=input("enter the team name: ")
is_genius=eval(input("is g or not: "))
              
print(player_name +" whose age is " + str(age) + ". the batting average is" + str(average) + ". Plays for " + team + "is a "+ str(is_genius) +" genius")

'''
'''
string
-syntax:
    ref=f"string with a placeholder {variable_name}"

adv:
   -automatically convert types(no need for str())
   -easier to read
   -supports expression inside{}       
'''
'''
print(f"{player_name} whose age is {age}. the batting average {average}. Plays for {team} is a {is_genius} genius")


statement = f"hello {num1}{num2}"
print(statement)
'''

'''

2nd using format() Method
syntax:
    "string with {} placeholders" .format(valuesplayer_name= input("Enter the player name:")
'''
player_name= input("Enter the player name:")
age = int(input("Enter the age:"))
average = float(input("Enter the Average:"))
team = input("Enter the Team Name:")
is_genius =eval(input(""))
hello ="{} whose age is {} and average is {} plays for {} is a {} genius.".format(player_name,age,average,team,is_genius)
print(hello)











