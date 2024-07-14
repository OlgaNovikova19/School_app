import unittest
from School_app.subject import Subject
from School_app.human import Human
from School_app.class_ import Class
from School_app.student import Student
from School_app.teacher import Teacher

"""
For testing:
1) Id assigning
2) Iteration in Class objects must be in alphabetical order.
3) Getting student/students by addressing Class object by [str].
 Returned students have name or lastname equal or beginning with this string.
The result is in alphabetical ascending order.
4) Check letter and grade of Class objects.
 Letter should be Cyrillic capitalized and single. It can be also None.
 Grade should be int greater or equal than 1 and minder or equal than 11. It can be also None.
5) Realisation of list methods for Class objects:
- append (add 1 student to class) -> add_student
- extend (add several students to class) -> add_students
- remove (remove a student from a class) -> remove_student, remove_students (removing several students as a list)
- pop (to delete a student from one class and be ready to insert it in another class) -> pop_student
- clear (remove all students from a class) -> clear_class
- len ->  get_size_class
"""


class TestID(unittest.TestCase):
    CORRECT_IDs = [0, 1, 2, 3, None]
    WRONG_IDs = [1.5, '', 'hello', [1, 2, 3]]
    REPEAT_IDs = [41, 57]

    def test_set_id(self):

        for value in self.CORRECT_IDs:
            if value not in Human.ids:
                test_human = Human('test_name', 'test_lastname', value)

        for value in self.REPEAT_IDs:
            try:
                test_human2 = Human('test_name', 'test_lastname', value)
                test_human3 = Human('test_name1', 'test_lastname1', value)
            except AttributeError:
                print('Attribute error was caught when trying to create Human object with equal ids')
            else:
                raise AssertionError(f'Human object was created with equal id format {value}')

        for value in self.WRONG_IDs:
            try:
                test_human_wrong = Human('test_name', 'test_lastname', value)
            except AttributeError:
                print(f'Attribute error was caught when trying to create Human object with wrong id {value}')
            else:
                raise AssertionError(f'Human object was created with wrong id format {value}')

    def test_namesakes_ids(self):
        test_h = Human('test_name1', 'test_lastname2')
        test_h_namesake = Human('test_name1', 'test_lastname2')
        self.assertNotEqual(test_h.get_id(), test_h_namesake.get_id(),
                            'Creation of Human objects with equal names and lastnames leads to creation of equal id')



class TestClassIteration(unittest.TestCase):
    student_Anya = Student('Anna', 'Petrova')
    student_Masha = Student('Maria', 'Petrova')
    stud = Student('Mikhail', 'Borisov')
    stud1 = Student('Mikhail', 'Romanov')
    stud2 = Student('Valerii', 'Chudnov')
    teacher_algebra_geometry = Teacher('Karina', 'Vasilieva', [Subject.ALGEBRA, Subject.GEOMETRY])
    cl = Class(teacher_algebra_geometry, [student_Masha, student_Anya], 2, 'А')
    cl_test = Class(teacher_algebra_geometry, [student_Masha, stud, stud1, stud2], 2, 'А')


    def test_iter_students_with_same_lastname(self):
        expected_order = [self.student_Anya, self.student_Masha]
        index_expected = 0

        for student in self.cl:
            self.assertEqual(student, expected_order[index_expected], 'Iteration of students with equal lastnames is wrong')
            index_expected += 1

    def test_iter_students_diff_lastnames(self):
        expected_order_test = [self.stud, self.stud2, self.student_Masha, self.stud1]
        index_expected_test = 0

        for student in self.cl_test:
            self.assertEqual(student, expected_order_test[index_expected_test], 'Iteration of students with different lastnames is wrong')
            index_expected_test += 1


class TestClassGetStudent(unittest.TestCase):
    def test_finding_one_stud(self):
        student_Elesei_Penkin = Student('Elesei', "Penkin")
        student_Elena_Penkina = Student('Elena', "Penenkova")
        teacher_music = Teacher('Aleksei', "Penkin")
        cl_find_stud = Class(teacher_music, [student_Elesei_Penkin], 7, 'В')

        print(cl_find_stud['Elesei'])

        self.assertEqual(cl_find_stud['Elesei'], [student_Elesei_Penkin], 'Finding one student by name wrong')

        self.assertEqual(cl_find_stud['Eles'], [student_Elesei_Penkin],
                         'Finding one student by beginning of the name wrong')
        self.assertEqual(cl_find_stud['Penkin'], [student_Elesei_Penkin], 'Finding one student by lastname wrong')
        self.assertEqual(cl_find_stud['Penk'], [student_Elesei_Penkin],
                         'Finding one student by beginning of the lastname wrong')

    def test_finding_students_sorted_and_wrong_names(self):
        student_Elena_Perova = Student('Elena', 'Perova')
        student_Alena_Petrova = Student('Alena', 'Petrova')
        student_Alla_Perieva = Student('Alla', 'Perieva')
        student_Aleksandr_Petrushkin = Student('Aleksandr', 'Petrushkin')
        student_Aleksei_Petrushkin = Student('Aleksei', 'Petrushkin')
        student_Alla_Perova = Student('Alla', 'Perova')

        teacher_geometry = Teacher('Elena', 'Petrova', [Subject.GEOMETRY])
        class_get_stud_test = Class(teacher_geometry,
                                    [student_Alla_Perieva, student_Aleksandr_Petrushkin, student_Alla_Perova, student_Aleksei_Petrushkin, student_Elena_Perova, student_Alena_Petrova],
                                    10, 'Б')



        expected_Petr_substr = [student_Alena_Petrova, student_Aleksandr_Petrushkin, student_Aleksei_Petrushkin]
        expected_Perova_str = [student_Alla_Perova, student_Elena_Perova]
        expected_Aleks_substr = [student_Aleksandr_Petrushkin, student_Aleksei_Petrushkin]
        expected_Alla_str = [student_Alla_Perieva, student_Alla_Perova]

        self.assertEqual(class_get_stud_test['Petr'], expected_Petr_substr,
                         'Finding students by the beginning of the lastname and sorting not correct')
        self.assertEqual(class_get_stud_test['Perova'], expected_Perova_str,
                         'Finding students by the whole lastname and sorting not correct')
        self.assertEqual(class_get_stud_test['Aleks'], expected_Aleks_substr,
                         'Finding students by the beginning of the name and sorting not correct')
        self.assertEqual(class_get_stud_test['Alla'], expected_Alla_str,
                         'Finding students by the whole name and sorting not correct')

        class_get_stud_test = Class(teacher_geometry,
                                    [student_Alla_Perieva, student_Aleksandr_Petrushkin, student_Alla_Perova,
                                     student_Aleksei_Petrushkin, student_Elena_Perova, student_Alena_Petrova],
                                    10, 'Б')

        WRONG_NAMES = {'lena': 'end of name',
                       'le': 'middle of name',
                       'Anna': 'wrong whole name',
                       'ova': 'end of lastname',
                       'tr': 'middle of lastname',
                       'Semenova': 'wrong whole lastname',
                       'Petrushkina': 'wrong whole lastname containing as a beginning correct lastname'
                       }

        for name_key, value_str in WRONG_NAMES.items():
            with self.subTest(f'Testing finding students by {value_str}'):
                try:
                    class_get_stud_test[name_key]
                except AttributeError:
                    print('Attribute Error was caught: wrong format was used for search')
                else:
                    self.assertEqual(class_get_stud_test[name_key], [], f'Student {class_get_stud_test[name_key]} was wrongly found by {value_str} {name_key}')


class TestClassGradeLetter(unittest.TestCase):
    CORRECT_LETTERS = ['А', 'Б', 'Я', None]
    WRONG_LETTERS = [1, 1.5, 'Q', ';', 'д', 'Дл', '1', '1.5', 'F', 'g']
    CORRECT_GRADES = [1, 11, 8, 2, 10, None]
    WRONG_GRADES = [1.5, 0, -1, -11, 12, 'А', '1']
    teacher_algebra = Teacher('Alla', 'Lisina', [Subject.ALGEBRA])
    student1 = Student('Oleg', 'Dubrovin')
    student2 = Student('Daria', 'Komarova')
    test_students = [student1, student2]

    def test_set_letter(self):
        for value in self.CORRECT_LETTERS:
            test_class = Class(self.teacher_algebra, self.test_students, 9, value)

        for value in self.WRONG_LETTERS:
            try:
                test_class1 = Class(self.teacher_algebra, self.test_students, 9, value)
            except AttributeError:
                pass
            else:
                raise AssertionError(f'Class object was created with wrong letter format {value}')

    def test_set_grade(self):
        for value in self.CORRECT_GRADES:
            test_class = Class(self.teacher_algebra, self.test_students, value, 'А')

        for value in self.WRONG_GRADES:
            try:
                test_class1 = Class(self.teacher_algebra, self.test_students, value, 'А')
            except AttributeError:
                pass
            else:
                raise AssertionError(f'Class object was created with wrong grade format {value}')



class TestListMethodsForClass(unittest.TestCase):
    def test_add_student(self):
        student_Daria_Perepelkina = Student('Daria', 'Perepelkina')
        student_Mikhail_Sergeev = Student('Mikhail', 'Sergeev')
        student_Anna_Pavlova = Student('Anna', 'Pavlova')
        teacher_math = Teacher('Valentina', 'Aleksandrova', [Subject.MATH])
        class_test = Class(teacher_math, [student_Daria_Perepelkina], 3, 'Б')
        class_test2 = Class(teacher_math, [student_Anna_Pavlova], 3, 'А')

        class_test.add_student(student_Mikhail_Sergeev)
        self.assertEqual(class_test._students, [student_Daria_Perepelkina, student_Mikhail_Sergeev], f'adding a student as an object failed')
        class_test.add_student(class_test2['anna'])
        self.assertEqual(class_test._students, [student_Daria_Perepelkina, student_Mikhail_Sergeev, [student_Anna_Pavlova]],
                         f'adding a list with a student/students by name/lastname failed')


        try:
            class_test.add_student(student_Mikhail_Sergeev)
        except AttributeError:
            print('AttributeError was caught: attempt to add a student that is already in this class')
        else:
            self.assertEqual(class_test._students, [student_Daria_Perepelkina, student_Mikhail_Sergeev, [student_Anna_Pavlova]],
                             f'The student was added 2 times to this class')

    def test_add_students(self):
        student_Alla_Marinina = Student('Alla', 'Marinina')
        student_Mikhail_Korostilev = Student('Mikhail', 'Korostilev')
        student_Alena_Pastuhova = Student('Alena', 'Pastuhova')
        student_Alena_Orlova = Student('Alena', 'Orlova')
        student_Oleg_Mazurkin = Student('Oleg', 'Mazurkin')

        teacher_history = Teacher('Anna', 'Alekseeva', [Subject.HISTORY])
        teacher_math = Teacher('Valentina', 'Aleksandrova', [Subject.MATH])

        class_test_add_students = Class(teacher_history, [student_Alla_Marinina], 4, 'Б')
        class_test_add_students1 = Class(teacher_history, [], 5, 'Б')
        class_test_add_students2 = Class(teacher_history, [student_Oleg_Mazurkin], 6, 'А')
        class_test_from = Class(teacher_math, [student_Mikhail_Korostilev, student_Alena_Orlova], 4, 'А')

        class_test_add_students.add_students(class_test_from['korost'], class_test_from['Alena'])

        self.assertEqual(class_test_add_students._students, [student_Alla_Marinina, student_Mikhail_Korostilev, student_Alena_Orlova],
                         'adding several students found by names/lastnames as several objects failed')

        class_test_add_students1.add_students(student_Alena_Pastuhova, student_Oleg_Mazurkin)


        self.assertEqual(class_test_add_students1._students,
                         [student_Alena_Pastuhova, student_Oleg_Mazurkin],
                         'adding several students as several objects failed')

        class_test_add_students2.add_students([student_Mikhail_Korostilev, student_Alena_Orlova])
        self.assertEqual(class_test_add_students2._students,
                         [student_Oleg_Mazurkin, student_Mikhail_Korostilev, student_Alena_Orlova],
                         'adding several students as a list failed')

        class_test_add_students3 = Class(teacher_history, [student_Alena_Orlova], 7, 'Б')
        try:

            class_test_add_students3.add_students(student_Alla_Marinina, student_Mikhail_Korostilev, student_Alena_Orlova)
        except AttributeError:
            print('AttributeError was caught: attempt to add students with one/several students that are already in this class')
        else:
            self.assertEqual(class_test_add_students3._students,
                             [student_Alla_Marinina, student_Mikhail_Korostilev],
                             f'These students were added 2 times to this class')

    def test_get_size_class(self):
        student_Alla_Marinina = Student('Alla', 'Marinina')
        student_Mikhail_Korostilev = Student('Mikhail', 'Korostilev')
        student_Alena_Orlova = Student('Alena', 'Orlova')
        teacher_history = Teacher('Anna', 'Alekseeva', [Subject.HISTORY])
        class_test_len = Class(teacher_history, [student_Alla_Marinina, student_Mikhail_Korostilev, student_Alena_Orlova ], 6, 'А')

        self.assertEqual(class_test_len.get_size_class(), 3, 'wrong measurement of len of list of students')

    def test_clear_class(self):
        student_Alla_Marinina = Student('Alla', 'Marinina')
        student_Mikhail_Korostilev = Student('Mikhail', 'Korostilev')
        student_Alena_Orlova = Student('Alena', 'Orlova')
        teacher_history = Teacher('Anna', 'Alekseeva', [Subject.HISTORY])
        class_test_clear = Class(teacher_history,
                               [student_Alla_Marinina, student_Mikhail_Korostilev, student_Alena_Orlova], 7, 'А')
        empty_class_test_clear = Class(teacher_history,
                               [], 7, 'Б')

        class_test_clear.clear_class()
        self.assertEqual(class_test_clear.get_size_class(), 0, 'clear_class function doesn`t remove all students from the class')
        empty_class_test_clear.clear_class()
        self.assertEqual(empty_class_test_clear.get_size_class(), 0, 'clear_class function doesn`t work properly if the class is empty')

    def test_remove_student(self):
        student_Alena_Orlova = Student('Alena', 'Orlova')
        student_Alla_Marinina = Student('Alla', 'Marinina')
        student_Mikhail_Korostilev = Student('Mikhail', 'Korostilev')
        teacher_history = Teacher('Anna', 'Alekseeva', [Subject.HISTORY])
        class_test_remove = Class(teacher_history,
                                 [student_Alena_Orlova, student_Alla_Marinina, student_Mikhail_Korostilev],8, 'А')


        class_test_remove.remove_student(student_Alena_Orlova)
        self.assertEqual(class_test_remove._students, [student_Alla_Marinina, student_Mikhail_Korostilev],
                         'remove_student function doesn`t remove a student from the class')

        try:
            class_test_remove.remove_student(student_Alena_Orlova)
        except ValueError:
            print("ValueError was caught because the student wasn`t in the list")
        else:
            raise AssertionError('trying to remove a student that is already absent in the class gives no ValueError and changes the list of the students')


    def test_pop_student(self):
        student_Alena_Orlova = Student('Alena', 'Orlova')
        student_Alla_Marinina = Student('Alla', 'Marinina')
        student_Mikhail_Korostilev = Student('Mikhail', 'Korostilev')
        teacher_history = Teacher('Anna', 'Alekseeva', [Subject.HISTORY])
        class_test_pop = Class(teacher_history,
                                   [student_Alena_Orlova, student_Alla_Marinina, student_Mikhail_Korostilev], 9, 'А')


        stud = class_test_pop.pop_student('Alena')
        self.assertEqual(class_test_pop._students, [student_Alla_Marinina, student_Mikhail_Korostilev],
                             'trying to pop a student by name/lastname goes wrong')

        stud1 = class_test_pop.pop_student('Marinina')
        self.assertEqual(class_test_pop._students, [student_Mikhail_Korostilev],
                        'trying to pop a student by name/lastname goes wrong')

        stud2 = class_test_pop.pop_student('Korost')
        self.assertEqual(class_test_pop._students, [],
                         'trying to pop a student by name/lastname goes wrong')

        try:
            stud3 = class_test_pop.pop_student('Alena')
        except ValueError:
            print('ValueError caught while using pop_student function because this student is absent in this class')
        else:
            raise AssertionError('ValueError was not caught in the case of using pop_student function for a student absent in this class')

    def test_remove_students(self):
        student_Alena_Orlova = Student('Alena', 'Orlova')
        student_Alla_Marinina = Student('Alla', 'Marinina')
        student_Mikhail_Korostilev = Student('Mikhail', 'Korostilev')
        teacher_history = Teacher('Anna', 'Alekseeva', [Subject.HISTORY])
        class_test_remove_students = Class(teacher_history,
                               [student_Alena_Orlova, student_Alla_Marinina, student_Mikhail_Korostilev], 9, 'А')
        class_test_remove_students_empty = Class(teacher_history,[], 10,'А')
        students = [student_Alena_Orlova, student_Alla_Marinina]

        class_test_remove_students.remove_students(students)
        self.assertEqual(class_test_remove_students._students, [student_Mikhail_Korostilev],
                         'trying to remove several students as a list of student objects goes wrong')

        class_test_remove_students.remove_students([])
        self.assertEqual(class_test_remove_students._students, [student_Mikhail_Korostilev],
                         'trying to remove empty list of students goes wrong')

        class_test_remove_students.remove_students(None)
        self.assertEqual(class_test_remove_students._students, [student_Mikhail_Korostilev],
                         'using None as an argument instead of list of students goes wrong')

        class_test_remove_students.remove_students([student_Mikhail_Korostilev])
        self.assertEqual(class_test_remove_students._students, [],
                         'trying to remove 1 student as a list goes wrong')

        try:
            class_test_remove_students_empty.remove_students([student_Alena_Orlova, student_Alla_Marinina])
        except ValueError:
            print('ValueError was caught when trying to delete several students as a list from an empty class')
        else:
            raise AssertionError('ValueError was not caught when trying to delete several students from an empty class')

