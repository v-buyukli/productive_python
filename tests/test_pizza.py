from unittest.mock import patch

from ..fluent_python.python_methods import pizza, pizza_abstract, pizza_class, pizza_mixing, pizza_static


# pizza.py
def test_get_size():
    p = pizza.Pizza(size=30)
    assert p.get_size() == 30


# pizza_static.py
def test_mix_ingredients():
    result = pizza_static.Pizza.mix_ingredients(3, 5)
    assert result == 8


def test_cook():
    p = pizza_static.Pizza(cheese=2, vegetables=4)
    result = p.cook()
    assert result == 6


# pizza_class.py
def test_from_fridge():
    fridge = pizza_class.Fridge(cheese=2, vegetables=4)
    p = pizza_class.Pizza.from_fridge(fridge)
    assert p.ingredients == 6


def test_from_fridge_with_zero_values():
    fridge = pizza_class.Fridge(cheese=0, vegetables=0)
    p = pizza_class.Pizza.from_fridge(fridge)
    assert p.ingredients == 0


# pizza_abstract.py
def test_get_radius_concrete_method():
    class ConcretePizza(pizza_abstract.BasePizza):
        def get_radius(self):
            return 10

    concrete_pizza = ConcretePizza()
    assert concrete_pizza.get_radius() == 10


# pizza_mixing.py
def test_margherita_pizza():
    margherita_pizza = pizza_mixing.MargheritaPizza(name='Margherita', ingredients=['Tomato Sauce', 'Mozzarella'])
    assert margherita_pizza.name == 'Margherita'
    assert margherita_pizza.get_ingredients() == ['Tomato Sauce', 'Mozzarella']


def test_pepperoni_pizza():
    pepperoni_pizza = pizza_mixing.PepperoniPizza(
        name='Pepperoni', ingredients=['Tomato Sauce', 'Pepperoni', 'Mozzarella']
    )
    assert pepperoni_pizza.name == 'Pepperoni'
    assert pepperoni_pizza.get_ingredients() == ['Tomato Sauce', 'Pepperoni', 'Mozzarella']


def test_pizza_static_method():
    with patch.multiple(pizza_mixing.Pizza, __abstractmethods__=set()):
        special_pizza = pizza_mixing.Pizza.static_method()
        assert special_pizza.name == 'Special Pizza'
        assert special_pizza.ingredients == ['Special Sauce', 'Special Cheese', 'Special Toppings']


def test_pizza_class_method():
    with patch.multiple(pizza_mixing.Pizza, __abstractmethods__=set()):
        custom_pizza = pizza_mixing.Pizza.class_method(custom_ingredients=['Custom Ingredient1', 'Custom Ingredient2'])
        assert custom_pizza.name == 'Custom Pizza'
        assert custom_pizza.ingredients == ['Custom Ingredient1', 'Custom Ingredient2']
