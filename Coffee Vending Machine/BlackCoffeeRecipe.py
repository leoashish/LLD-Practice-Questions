from Recipe import Recipe
from Ingredient import Ingredient
from coffeeModel import CoffeeModel
from time import time


class BlackCoffeeRecipe(Recipe):
    def __init__(self, ingredients: dict[Ingredient, int]):
        self.ingredients = ingredients

    def make_coffee(self):
        print("Making Black Coffee")
