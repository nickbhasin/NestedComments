class User:

    def __init__(self, name, id) -> None:

        self.name = name
        self.id = id

    def getId(self):
        return self.id

    def setId(self, value):
        self.id = value

    def getName(self):
        return self.name

    def setName(self, value):
        self.name = value

