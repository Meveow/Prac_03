YEAR = 2022


class GuitarInfo:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = 0

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        self.age = YEAR - self.year
        return self.age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
