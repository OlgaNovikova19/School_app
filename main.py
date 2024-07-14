from subject import Subject
from human import Human
from class_ import Class
from student import Student
from teacher import Teacher


"""
1. Checking basic functionality of class Human
"""
h = Human('Aleksandr', 'Berezkin')
hh = Human('Vasilii', 'Elkin', 3)
print(h)
print(h.get_id(), hh.get_id())
"""The Human object is less than another one if lastname is less or if name is less"""
print(sorted([h, hh]))
print(hash(h))

"""
2. Checking basic functionality of class Student
"""
student_Anya = Student('Anna', 'Petrova')
print(student_Anya)
student_Masha = Student('Maria', 'Petrova')
stud = Student('Mikhail', 'Borisov')
""" Sorting order is inherited from class Human """
print(sorted([student_Anya,student_Masha, stud]))

"""
3. Checking basic functionality of class Teacher
"""
teacher_algebra_geometry  = Teacher('Karina', 'Vasilieva', [Subject.ALGEBRA, Subject.GEOMETRY])
print(teacher_algebra_geometry)
teacher_no_subjects = Teacher('Elena', 'Perova', [])
print(teacher_no_subjects)
""" Sorting order is inherited from class Human """
print(sorted([teacher_algebra_geometry, teacher_no_subjects]))

"""
4. Checking basic functionality of class Class
"""

"""
class_2A = Class(teacher_algebra_geometry, [])
print(class_2A)
class_2A.letter = 'B'
#class_2A.letter = 'CD'
#class_2A.letter = 'c'
print(class_2A.letter)

class_2A.grade = 5
#class_2A.grade = 12
#class_2A.grade = 0
#class_2A.grade = 5.5
#class_2A.grade = 11
#class_2A.grade = 1
print(class_2A.grade)

"""

t = Teacher('Maria', 'Vasilieva', [Subject.HISTORY, Subject.MATH])
cl = Class(t, [student_Masha, stud, student_Anya], 2, 'А')
print(cl._homeroom_teacher.name)
#print(cl._students)
#print(class_2A)
cl.write_csv("Class_inform.csv")
print("======================")
cl.read_csv("Class_inform.csv")
print("======================")
#cl.write_csv_user("Class_inform.csv")

print(student_Anya)
print(student_Masha)
print(stud)

""" Checking search for student if lastname or name is provided """
print(cl["Petrova"])
print(cl["Anna"])
print(cl["Mikhail"])
""" Checking that if 2 equal lastnames or names the output is sorted """
print(cl["Petrova"])

#Checking sorted output while running iteration. Object being less defined by the lastname as main condition and by the name if lastnames are equal """
#for i in cl:
 # print(i)

s

