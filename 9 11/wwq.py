import datetime

class Student:
    def __init__(self, name, surname, birthdate, height=160):
        if(type(name) != str):
            raise TypeError(f"Name must be a str type. Not a '{type(name)}'")
        if (type(surname) != str):
            raise TypeError(f"Surname must be a str type. Not a '{type(surname)}'")
        if (type(birthdate) != str):
            raise TypeError(f"Birthdate must be a str type. Not a '{type(birthdate)}'")


        birthdate_dt = datetime.datetime.strptime(birthdate, '%d.%m.%Y')
        if (birthdate_dt > datetime.datetime.now)():
            raise ValueError("Birthdate cannot be in the future")

        if (not isinstance(height, (int, float))):
            raise TypeError(f"Height must be an int or float. Not a '{type(height)}'")
        if (height <= 0):
            raise ValueError("Height must be greater than zero")

        self.name = name
        self.surname = surname
        self.birthdate = birthdate_dt
        self.height = height
        print(f"I am {self.name}")

    def printStudent(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Birthdate: {self.birthdate.strftime('%d.%m.%Y')}")
        print(f"Height: {self.height}")

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nBirthdate: {self.birthdate.strftime('%d.%m.%Y')}\nHeight: {self.height}\n"

    def __int__(self):
        age = (datetime.datetime.now() - self.birthdate)
        return int(age.days / 365)


# Creating objects
first_student = Student('vlad', 'karlinskij', '25.10.2006', 186)
second_student = Student('oleg', 'palkin', '25.5.2000', 220)

first_student.printStudent()

print('------------------------------')
print(type(first_student.__str__()))
print(first_student)
print('------------------------------')
print(type(first_student.__int__()))
print(int(first_student))

