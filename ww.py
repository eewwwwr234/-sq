class Student:
    print("Hi")

    def __init__(self, height=160, school=None):
        self.height = height
        self.school = school
        print("I am alive")

  def __bool__(self):
        return bool(self.school)


first_student = Student(186, "School A")
second_student = Student(220)

print(first_student.height)
print(second_student.height)

print(bool(first_student))
print(bool(second_student))

print('test')

print('test')
print('test')