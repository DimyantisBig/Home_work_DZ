class Person:
    def __init__(self, first_name, last_name, work):
        self.first_name = first_name
        self.last_name = last_name
        self.work = work

    def talk (self):
        return f'Hello, my name is {self.first_name} {self.last_name} and I am {self.work}.'

class Student (Person):
    def __init__(self,first_name, last_name, work, student_id,course,age):
        super().__init__(first_name, last_name, work)
        self.student_id = student_id
        self.course = course
        self.age = age

    def course_student (self, new_course):
        self.course = new_course
        return f'Course successfully changed to {new_course}.'

    def info_student (self):
        return (f'Student {self.first_name} {self.last_name},{self.age} year old. \n '
                f'His Student ID № {self.student_id}\n'
                f'Is studying at the course {self.course}  ')

class Teacher (Person):
    def __init__(self,first_name, last_name, work,subject, salary):
        super().__init__(first_name, last_name, work)
        self.subject = subject
        self.salary = salary

    def info_teacher (self, new_salary):
        self.salary = new_salary
        return f'Teacher {self.subject} {self.first_name} {self.last_name}, your salary is {self.salary}.'



person = Person('Alis', 'Purple', 'Principal')
print(person.talk())
print('---'*10)
student = Student('John', 'Dulitl', 'student', 'M808987', 'Mathematics', 25)
print(student.info_student())
print('---'*10)
print(student.course_student('Physics'))
print('---'*10)
print(student.info_student())
print('---'*10)
teacher = Teacher('Juliya', 'Watson', 'teacher', 'Mathematics', 50000)
print(teacher.info_teacher(55000)) # Обновляем и проверяем зарплату









