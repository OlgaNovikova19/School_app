class Human:
    name: str = ''
    last_name: str = ''
    _id = None
    ids = set()

    def __init__(self, name, last_name, id=None):
        """if id in Human.ids:
          raise Exception("Переданный id уже существует!")
        elif id is None:
          if len(Human.ids) >= 1:
            id = max(Human.ids)+1
          else:
            id = 1
        self._id = id"""
        id = self.id_check_generation(id)
        self._id = id
        Human.ids.add(id)
        self.name = name
        self.last_name = last_name

    @staticmethod
    def id_check_generation(id = None):
      if id in Human.ids:
          raise Exception("Переданный id уже существует!")
      elif id is None:
        if len(Human.ids) >= 1:
          id = max(Human.ids)+1
        else:
          id = 1
      return id

    def get_id(self):
      return self._id

    def __lt__(self, other):
      if ''.join([self.last_name, self.name]) < ''.join([other.last_name, other.name]):
        return self < other
      return other < self

    def __hash__(self):
      return hash(self._id)

    def __repr__(self):
      return f'class<Human>object representation: name = {self.name}, last_name = {self.last_name}, _id = {self._id}'

    def __str__(self):
      return f'Human with name {self.name}, lastname {self.last_name} and id number {self._id}'

