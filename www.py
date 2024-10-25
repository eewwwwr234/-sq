# ніби то шаблон
class Student:
    pass


class Student:
    print("Hi")

    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def display_info(self):
        print(f"Ім'я: {self.first_name}")
        print(f"Прізвище: {self.last_name}")
        print(f"Дата народження: {self.date_of_birth}")

    def __Student__(self, height=160):
        self.height = height
        print("I am alive")

    student1 = Student("Іван", "Петров", "01.01.2000")
    student2 = Student("Марія", "Іванова", "15.05.1999")

# створення об'єкта
first_student = Student(186)
second_student = Student(220)

#вивети інормацію про їого зріст
print(first_student.height)
print(second_student.height)







# Створення двох об'єктів класу Student


# Виведення інформації про студентів

