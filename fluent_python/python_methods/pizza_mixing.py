from abc import ABC, abstractmethod


class Pizza(ABC):
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    @abstractmethod
    def get_ingredients(self):
        pass

    @staticmethod
    def static_method():
        return Pizza('Special Pizza', ['Special Sauce', 'Special Cheese', 'Special Toppings'])

    @classmethod
    def class_method(cls, custom_ingredients):
        return cls('Custom Pizza', custom_ingredients)


class MargheritaPizza(Pizza):
    def get_ingredients(self):
        return self.ingredients


class PepperoniPizza(Pizza):
    def get_ingredients(self):
        return self.ingredients
