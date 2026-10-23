class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        return f'{self.name}'
class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
    def info(self):
        return f'{self.name} , {self.group}'
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def info(self):
        return f'{self.name} , {self.subject}'
class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
    def add_student(self, student):
        self.students.append(student)


course2 = Course("Maths", "Jones")

teacher = Teacher("Komarov", "Computer Science")
student1 = Student("Anna", "10IT")
person1 = Person("John")
student2 = Student("Bob", "10IT")
course2.add_student(student1)
course2.add_student(student2)

for student in course2.students:
    print(student.info())
# print(course.name)
# print(course.teacher)
# print(course.students)



# people = [Person("Ivan"), Student("Anna", "10IT") , Teacher("Komarov" , "Math"),  Student("Sophii", "10MA")]
# for p in people:
#     print(p.info())
# print(student.name)
# print(student.group)
# print(person1.info())
# print(person1.info())
# print(student.info())
# print(teacher.info())

# print(isinstance(student, Person))