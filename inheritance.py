class SpaceObject:
    def __init__(self, name=None):
        self.name = name

class Planet(SpaceObject):
    def __init__(self, name, *population):
        super().__init__(name)
        self.population = population or []

    def __repr__(self):
        return f"На планете {self.name} обитают {', '.join(arg.name for arg in self.population)}"

class Animal():
    def __init__(self, name=None):
        self.name = name

class Elephant(Animal):
    def __init__(self, name, gender=None, weight=None):
        super().__init__(name)
        self.gender = gender
        self.weight = weight

    def eat(self, food):
        self.food = food
        return f"{self.name} только что съел {self.food}"

class Monkey(Animal):
    def __init__(self, name, gender=None, weight=None):
        super().__init__(name)
        self.gender = gender
        self.weight = weight

    def eat(self, food):
        self.food = food
        return f"{self.name} только что съела {self.food}"

class Kangaroo(Animal):
    def __init__(self, name, gender=None, weight=None):
        super().__init__(name)
        self.gender = gender
        self.weight = weight

    def carry_baby(self):
        if self.gender == "female":
            return f"Самка {self.name} вынашивает детеныша"
        else:
            return f"Самец {self.name} не может вынашивать детеныша"

if __name__ == "__main__":
    indian_elephant = Elephant('Слон Kristy', 'female', '4000')
    orangutan = Monkey('Обезьяна Bucky', 'male', '80')
    great_kangaroo = Kangaroo('Кенгуру Lily', 'female', '70')
    red_kangaroo = Kangaroo('Kенгуру Mike', 'male')
    earth = Planet("Земля", indian_elephant, orangutan, great_kangaroo, red_kangaroo)
    print(earth)
    print(orangutan.eat("банан"))
    print(indian_elephant.eat("трава"))
    print(red_kangaroo.carry_baby())
    print(great_kangaroo.carry_baby())