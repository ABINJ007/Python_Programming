class Student:
    course = "Pythonfullstack"  # classvariable
    roomnumber = 101  # classvariable2


Student.institute = "DCL"  # classvariable3
print(Student.__dict__)
print(Student.course)
print(Student.roomnumber)
Student.institute = "Dhee coding lab"
print(Student.institute)
Student.institute="Dhee coding lab"

class currency:
    authority="RBI"
    signature="Governor"
    approved_by="centralGovt"
print(currency.authority)
print(currency.signature)
print(currency.approved_by)

currency.authority="Reserve Bank of India"
print(currency.authority)

