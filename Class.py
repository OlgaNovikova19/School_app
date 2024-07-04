from enum import Enum
from typing import List
import csv
import os


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
        elif grade == None:
            return grade
        else:
            raise Exception("Класс должен быть целым числом в интервале от 1 до 11 включительно!")

    @staticmethod
    def check_letter(letter):
        if letter == None:
            return letter
        elif letter.istitle() and len(letter) == 1:
            return letter
        else:
            raise Exception("Наименование класса должно состоять из 1 заглавной буквы!")

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
        raise Exception("Класс должен быть целым числом в интервале от 1 до 11 включительно!")

    @property
    def letter(self):
       return self._letter

    @letter.setter
    def letter(self, letter):
      if len(letter) == 1 and letter.istitle() :
        self._letter = letter
      else:
        raise Exception("Наименование класса должно состоять из 1 заглавной буквы!")"""

    def __iter__(self):
        return iter(sorted(self._students))

    def __getitem__(self, name):
        return [i for i in sorted(self._students) if name == i.name or name == i.last_name]

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
