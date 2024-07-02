from enum import Enum

class Subject(Enum):
    MATH = 'Математика'
    RUSSIAN_LANG = 'Русcкий Язык'
    FOREIGN_LANG = 'Английский Язык'
    SECOND_FOREIGN_LANG = 'Немецкий язык'
    COMPUTER_SCIENCE = 'Информатика'
    ALGEBRA = 'Алгебра'
    GEOMETRY = 'Геометрия'
    LITERATURE = 'Литература'
    HISTORY = 'История'
    GEOGRAPHY = 'География'
    CHEMISTRY = 'Химия'
    BIOLOGY = 'Биология'
    PHYSICS = 'Физика'
    PHYSICAL_EDUCATION = 'Физкультура'
    MUSIC = 'Музыка'
    SOCIAL_SCIENCES = 'Обществознание'
    HISTORY_OF_THE_CITY = 'История города'
    DRAWING = 'Рисование'
    TECHNOLOGY = 'Труд'
    HOME_ECONOMICS = 'Домоводство'
    TECHNICAL_DRAWING = 'Черчение'
    LIFE_SAFETY = 'ОБЖ'
    CULTURE_STUDIES = 'Культурология'
    READING = 'Чтение'
    NATURAL_HISTORY = 'Природоведение'
    PLANNED_EXCURSION = 'Экскурсия по плану'
    HOMEROOM_PERIOD = 'Классный час'

    def __repr__(self):
      return f'class<Subject>subobject representation: name = {self.name}, value = {self.value}'

    def __str__(self):
      return self.value

#print(Subject.MATH.name)
#print(Subject.MATH.value)
#Subject.MATH.ALGEBRA.GEOGRAPHY
#print(Subject.MATH)
#Subject.MATH