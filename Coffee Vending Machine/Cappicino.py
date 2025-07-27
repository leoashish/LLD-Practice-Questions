from Recipe import Recipe
from Ingredient import Ingredient
from coffeeModel import CoffeeModel


class CappicinoRecipe(Recipe):
    def __init__(self, ingredients: dict[Ingredient, int]):
        self.ingredients = ingredients

    def make_coffee(self):
        print("Making Cappicino")
