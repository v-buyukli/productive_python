class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def from_fridge(cls, fridge):
        return cls(fridge.get_cheese() + fridge.get_vegetables())


class Fridge:
    def __init__(self, cheese, vegetables):
        self.cheese = cheese
        self.vegetables = vegetables

    def get_cheese(self):
        return self.cheese

    def get_vegetables(self):
        return self.vegetables
