# Player class

class Player:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    @property
    def uid(self):
        return self.id

    @property
    def name(self):
        return self.name

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"
