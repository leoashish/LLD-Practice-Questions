from Ingredient import Ingredient


class Inventory:
    def __init__(self):
        self.ingredients: dict[Ingredient, int] = {}

    def add_ingredient(self, ingredient: Ingredient, qty: int):
        self.ingredients[ingredient] = qty
