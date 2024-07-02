class Student(Human):
    _class: Class = None
    name: str = ''
    last_name: str = ''
    _id = None

    def __init__(self, name, lastname, class_=None, id_stud=None):
        super().__init__(name, lastname, id_stud)
        self._class = class_

    def set_class(self, Class):
        self._class = Class

    def get_class(self):
        return self._class

    def __lt__(self, other):
        return super().__lt__

    def __repr__(self):
        return f'class<Student>object representation: name = {self.name}, last_name = {self.last_name}, _class = {self._class}, _id = {self._id}'

    def __str__(self):
        return f'Student with name {self.name}, lastname {self.last_name}, class {self._class} and id {self._id}'