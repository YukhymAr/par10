#1
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         return f'{self.name}'
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#     def info(self):
#         return f'Учень: {self.name} , група: {self.group}'
#
# student1 = Student('Anna', '10IT')
# print(student1.info())

#2
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         return f'{self.name}'
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#     def info(self):
#         return f'Учень: {self.name} , група: {self.group}'
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#     def info(self):
#         return f'Викладач: {self.name} , Предмет: {self.subject}'
#
# student1 = Student('Anna', '10IT')
# student2 = Student('s1mple', '10MA-IT')
# teacher1 = Teacher('Ivan Komarov', 'CS')
#
#
# print(teacher1.info())
# print(student1.info())
# print(student2.info())

#3
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         return f'{self.name}'
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#     def info(self):
#         return f'{self.name}, група: {self.group}'
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#     def info(self):
#         return f'{self.name} ({self.subject})'
# class Course:
#     def __init__(self, title, teacher):
#         self.title = title
#         self.teacher = teacher
#         self.students = []
#     def add_student(self, student):
#         for s in self.students:
#             if s.name == student.name:
#                 print(f"Студент '{student.name}' вже є на курсі!")
#                 return
#         self.students.append(student)
#     def remove_student(self, name):
#         self.students = [s for s in self.students if s.name != name]
#     def show_students(self):
#         print(f"Курс: {self.title}")
#         print(f"Викладач: {self.teacher.info()}")
#         print("Студенти:")
#         for index, student in enumerate(self.students, 1):
#             print(f"{index}. {student.info()}")
# teacher1 = Teacher('Іван Комаров', 'Counter Strike')
# course1 = Course('Python', teacher1)
#
# s1 = Student('Анна', '10IT')
# s2 = Student('s1mple', '10MA-IT')
# s3 = Student('Максим', '10IT')
# s4 = Student('Софія', '10MA')
#
# course1.add_student(s1)
# course1.add_student(s2)
# course1.add_student(s3)
# course1.add_student(s4)
# course1.remove_student('Максим')
# course1.show_students()


#4
import os

class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        return f'{self.name}'

class Student(Person):
    def __init__(self, name, group, grades=None):
        super().__init__(name)
        self.group = group
        self.grades = grades if grades is not None else []
    def add_grade(self, grade):
        if 1 <= grade <= 12:
            self.grades.append(grade)
        else:
            print("Оцінка має бути від 1 до 12")
    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    def info(self):
        return f'{self.name}, група: {self.group}'

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def info(self):
        return f'{self.name}, предмет: {self.subject}'

class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []
    def add_student(self, student):
        for s in self.students:
            if s.name == student.name:
                return
        self.students.append(student)
    def remove_student(self, name):
        self.students = [s for s in self.students if s.name != name]
    def find_student(self, name):
        for s in self.students:
            if s.name == name:
                return s
        return None
    def add_grade_to_student(self, name, grade):
        student = self.find_student(name)
        if student:
            student.add_grade(grade)
    def show_students(self):
        print(f"Курс: {self.title}")
        print(f"Викладач: {self.teacher.info()}")
        print("Студенти:")
        for index, student in enumerate(self.students, 1):
            print(f"{index}. {student.info()}")
    def show_rating(self):
        def get_average(student):
            return student.average()
        sorted_students = sorted(self.students, key=get_average, reverse=True)
        print("Рейтинг:")
        for index, student in enumerate(sorted_students, 1):
            print(f"{index}. {student.name} — {student.average():.2f}")
    def save_data(self, filename="course_data.txt"):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for student in self.students:
                    grades_str = ",".join(map(str, student.grades))
                    f.write(f"{student.name} ; {student.group} ; {grades_str}\n")
            print("Дані збережено")
        except Exception as e:
            print(f"Помилка збереження: {e}")
    def load_data(self, filename="course_data.txt"):
        if not os.path.exists(filename):
            return
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(";")
                    if len(parts) >= 2:
                        name = parts[0]
                        group = parts[1]
                        grades = []
                        if len(parts) > 2 and parts[2]:
                            for g in parts[2].split(","):
                                try:
                                    grades.append(int(g))
                                except ValueError:
                                    pass
                        student = Student(name, group, grades)
                        self.students.append(student)
            print("Після нового запуску студенти та оцінки відновлені")
        except Exception as e:
            print(f"Помилка читання: {e}")

teacher1 = Teacher('Іван Комаров', 'Python')
course1 = Course('Python', teacher1)

s1 = Student('Анна', '10IT', [12])
s2 = Student('s1mple', '10MA-IT', [11])
s3 = Student('Максим', '10IT', [10])
s4 = Student('Софія', '10MA', [9])

course1.add_student(s1)
course1.add_student(s2)
course1.add_student(s3)
course1.add_student(s4)

course1.load_data()

while True:
    print("1 — показати курс")
    print("2 — додати студента")
    print("3 — видалити студента")
    print("4 — знайти студента")
    print("5 — виставити оцінку")
    print("6 — показати рейтинг")
    print("7 — зберегти дані")
    print("0 — вихід")
    choice = input("Виберіть пункт: ")
    if choice == '1':
        course1.show_students()
    elif choice == '2':
        name = input("Введіть ПІБ: ")
        group = input("Введіть групу: ")
        course1.add_student(Student(name, group))
    elif choice == '3':
        name = input("Введіть ПІБ: ")
        course1.remove_student(name)
    elif choice == '4':
        name = input("Введіть ПІБ: ")
        student = course1.find_student(name)
        if student:
            print(student.info())
        else:
            print("Не знайдено")
    elif choice == '5':
        name = input("Введіть ПІБ: ")
        try:
            grade = int(input("Введіть оцінку: "))
            course1.add_grade_to_student(name, grade)
        except ValueError:
            print("Неправильна оцінка")
    elif choice == '6':
        course1.show_rating()
    elif choice == '7':
        course1.save_data()
    elif choice == '0':
        break
    else:
        print("Виберіть інше")
# Просто жах...