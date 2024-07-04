from typing import List
from Human import Human
from Subject import Subject
from Class import Class


class Teacher(Human):
    _homeroom_class: Class | None = None
    _subjects: List[Subject] = []
    name: str
    last_name: str
    _id = None
    def __init__(self, name, last_name, subjects=None, id_teacher=None):
        super().__init__(name, last_name, id_teacher)
        if subjects is not None:
            self._subjects = subjects
        else:
            self._subjects = []
        self.name = name
        self.last_name = last_name

    def set_class(self, Class):
        _homeroom_class = Class

    def get_class(self):
        return _homeroom_class

    def __lt__(self, other):
        return super().__lt__(other)

    def __repr__(self):
        return f'class<Teacher>object representation: name = {self.name}, last_name = {self.last_name}, _subjects = {self._subjects},  _homeroom_class = {self._homeroom_class}'

    def __str__(self):
        subjects_list = []
        subjects_str = ''
        if not self._subjects:
            subjects_str = 'None'
        else:
            for subj in self._subjects:
                subjects_list.append(subj.value)
            subjects_str = ', '.join(subjects_list)
        return f'Teacher with name {self.name}, lastname {self.last_name}, subjects {subjects_str}, homeroom class {self._homeroom_class} and id {self._id}'