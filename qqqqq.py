class Student:
    def __init__(self, student_id, full_name, variant, group):
        self.student_id = student_id
        self.full_name = full_name
        self.variant = variant
        self.group = group

# Загрузка списка студентов из файла
students = []
with open('students.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(';')
        student_id = int(data[0].strip())
        full_name = data[1].strip()
        variant = int(data[2].strip())
        group = int(data[3].strip())
        student = Student(student_id, full_name, variant, group)
        students.append(student)

# Вывод отформатированной информации о студентах
print('-------------------------------------------------------------')
print('| ID | FIO                                |  VARIANT | GROUP |')
print('-------------------------------------------------------------')
for student in students:
    print(f'| {student.student_id:<2} | {student.full_name:<34} | {student.variant:<8} | {student.group:<5} |')
print('-------------------------------------------------------------')