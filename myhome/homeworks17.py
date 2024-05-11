grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3],[5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#Преобразуем в список и расположим студентов по влфавиту
students_ = sorted(list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}))
#Проверим наш список
print(students_)
#Создадим пустой словарь
student_grade = {}
n = 0
#Заполним наш словарь
for i in students_:
    student_grade[students_[n]] = float(sum(grades[n])) / len(grades[n])
    n += 1
print(student_grade)
