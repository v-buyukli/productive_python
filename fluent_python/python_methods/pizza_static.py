class Pizza:
    def __init__(self, cheese, vegetables):
        self.cheese = cheese
        self.vegetables = vegetables

    @staticmethod
    def mix_ingredients(x, y):
        return x + y

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)
