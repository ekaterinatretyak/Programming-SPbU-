class SpaceObject:
    def __init__(self, name=None):
        self.name = name

class Planet(SpaceObject):
    def __init__(self, name, population=None):
        super().__init__(name)
        self.population = population or []

class Animal():
    def __init__(self, name=None):
        self.name = name

class Elephant(Animal):
    def __init__(self, name, gender, weight):
        super().__init__(name)
    def eat(self, ):


class Monkey(Animal):
    def __init__(self, name, gender, weight):
        super().__init__(name)

    def eat(self, banana):


class Kangaroo(Animal):
    def __init__(self, name, gender, weight):
        super().__init__(name)

    def carry_baby(self, baby):
        


Earth = Planet()