from typing import List
import csv
import os
import string
from collections.abc import Iterable

class Class(list):
    _grade: int = 1
    _letter: str = 'A'
    _students: List["Student"] = []
    _homeroom_teacher: "Teacher"

    def __init__(self, homeroom_teacher, students, grade=None, letter=None):
        self._homeroom_teacher = homeroom_teacher
        self._students = list(students)
        self._grade = self.check_grade(grade)
        self._letter = self.check_letter(letter)

    @staticmethod
    def check_grade(grade):
        if type(grade) == int and grade >= 1 and grade <= 11:
            return grade
        elif grade is None:
            return grade
        else:
            raise AttributeError("Класс должен быть целым числом в интервале от 1 до 11 включительно!")

    @staticmethod
    def check_letter(letter):
        RUS_LETTERS_UPPER = [chr(i) for i in range(ord('А'), ord('Я')+1)]
        ENG_LETTERS_UPPER = list(string.ascii_uppercase)
        if letter is None or letter in RUS_LETTERS_UPPER:
            return letter
        elif letter in ENG_LETTERS_UPPER:
            raise AttributeError("Введена буква латинского алфавита!")
        else:
            raise AttributeError("Наименование класса должно состоять из 1 заглавной буквы!")

    def get_grade(self):
        return self._grade

    def set_grade(self, grade):
        self._grade = self.check_grade(grade)

    def get_letter(self):
        return self._letter

    def set_letter(self, letter):
        self._letter = self.check_letter(letter)

    grade = property(get_grade, set_grade)
    letter = property(get_letter, set_letter)

    """@property
    def grade(self):
      return self._grade

    @grade.setter
    def grade(self, grade):
      if type(grade)== int and grade >=1 and grade <= 11:
        self._grade = grade
      else:
        raise AttributeError("Класс должен быть целым числом в интервале от 1 до 11 включительно!")

    @property
    def letter(self):
       return self._letter

    @letter.setter
    def letter(self, letter):
      if len(letter) == 1 and letter.istitle() :
        self._letter = letter
      else:
        raise AttributeError("Наименование класса должно состоять из 1 заглавной буквы!")"""

    def __iter__(self):
        return iter(sorted(self._students))

    def __getitem__(self, name: str) -> list:
        ENG_LETTERS_LOWER_ = list(string.ascii_lowercase)
        result = []

        if type(name) is not str:
            raise AttributeError('Search for students of the class must be made with the string format')
        else:
            for ch in name:
                if ch.lower() not in ENG_LETTERS_LOWER_:
                    raise AttributeError('Search for students of the class must be made with Latin Alphabet')

        for i in sorted(self._students):
            if i.name.lower().startswith(name.lower()) or i.last_name.lower().startswith(name.lower()):
                result.append(i)
        return result

    def add_student(self, student) -> None:
        if student not in self._students:
            self._students.append(student)
        else:
            raise AttributeError(f'This student {student} was not added to class {self}. He studies already in this class')

    def add_students(self, *args) -> None:
        temp_list = []
        students = list(args)

        for student in students:
            if student not in self._students:
                if isinstance (student, Iterable):
                    for i in student:
                        self._students.append(i)
                else:
                    self._students.append(student)
            else:
                temp_list.append(student)

        if len(temp_list) > 0:
            raise AttributeError(f'These students {temp_list} were not added to class {self}')


    def remove_student(self, student)-> None:
        """Student objects are unique because of id,
        so no same objects are left after remove() """
        self._students.remove(student)

    def remove_students(self, students:list)-> None:
        if students is not None:
            for student in students:
                self._students.remove(student)
        else:
            return

    def pop_student(self, name: str):
        found_students = self[name]
        if len(found_students) > 0:
            student = self[name][0]
            index = self._students.index(student)
            return self._students.pop(index)
        else:
            raise ValueError("No student with such name/lastname for deletion")


    def clear_class(self):
        self._students.clear()

    def get_size_class(self) -> int:
        return len(self._students)



    @staticmethod
    def read_csv(filename):
        recover_header = []
        recover_body = []
        with open(filename) as f:
            file = csv.reader(f)
            for i, line in enumerate(file):
                if i == 0:
                    recover_header = line

                elif len(line) == 0:
                    continue

                else:
                    recover_body = line

            print(dict(zip(recover_header, recover_body)))

    '''def write_csv_user(self, filename):
      field_names = ['_grade', '_letter', '_students', '_homeroom_teacher']
      students_inf = []
      for student in self._students:
         students_inf.append(' '.join([student.name, student.last_name, str(student._id)]))
      with open(filename, "w") as f:
        csv.writer(f).writerow(field_names)
        csv.writer(f).writerow([f"{self._grade}", f"{self._letter}", f"{students_inf}", ' '.join([self._homeroom_teacher.name, self._homeroom_teacher.last_name])])
        #print(f"{self._grade}", f"{self._letter}", f"{students_inf}", ' '.join([self._homeroom_teacher.name, self._homeroom_teacher.last_name]))'''

    # if os.path.exists(filename):
    # print("File was successfully created: %s" % os.path.abspath(filename))

    def write_csv(self, filename):
        field_names = ['_grade', '_letter', '_students', '_homeroom_teacher']
        with open(filename, "w") as f:
            row_to_save = [f"{self._grade}", f"{self._letter}", f"{self._students}", f"{self._homeroom_teacher}"]
            csv.writer(f).writerow(field_names)

            csv.writer(f).writerow(row_to_save)
            # print(field_names)
            # print(f"{self._grade}", f"{self._letter}", f"{self._students}", f"{self._homeroom_teacher}")

    def __repr__(self):
        return f'class<Class>object representation: _grade = {self._grade}, _letter = {self._letter}, _students = {self._students}, _homeroom_teacher = {self._homeroom_teacher}'

    def __str__(self):
        return f'Class with grade {self._grade}, letter {self._letter}, students {self._students}, homeroom teacher {self._homeroom_teacher}'
