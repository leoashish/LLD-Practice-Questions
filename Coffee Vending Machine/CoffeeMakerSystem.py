from Ingredient import Ingredient
from coffeeModel import CoffeeModel
from Inventory import Inventory
from Recipe import Recipe
from typing import Optional


class CoffeeMakerSystem:
    def __init__(self):
        self.coffeeTypes: list[CoffeeModel] = []
        self.inventory: Inventory = Inventory()
        self.insertedAmount = 0
        self.currentCoffee: Optional[CoffeeModel] = None

    def insert_coffee_types(self, coffee: CoffeeModel):
        self.coffeeTypes.append(coffee)

    def fill_inventory(self, ingredient: Ingredient, qty: int):
        self.inventory.add_ingredient(ingredient, qty)

    def selectCoffee(self, coffee: CoffeeModel):
        if not self.check_ingredient_avalability(coffee):
            raise ValueError("Not enough ingredient!!")
        self.currentCoffee = coffee

    def receive_payment(self, amount: int):
        self.insertedAmount += amount

    def give_out_change(self) -> None:
        if self.currentCoffee == None:
            raise ValueError("No coffee selected")

        change = self.insertedAmount - self.currentCoffee.cost
        self.insertedAmount = 0
        print(f"Please receive change {change}.")

    def brew_coffee(self):
        if self.currentCoffee == None:
            raise ValueError("No Coffee Selected!!!")
        # Deduct the ingredients
        recipe = self.currentCoffee.recipe
        for item, qty in recipe.ingredients.items():
            self.inventory.ingredients[item] -= qty

        self.currentCoffee.recipe.make_coffee()

    def check_ingredient_avalability(self, coffee: CoffeeModel) -> bool:
        # Check for inventory
        recipe = coffee.recipe
        for ing, qty in recipe.ingredients.items():
            if self.inventory.ingredients[ing] < qty:
                return False
        return True

    def dispence_coffee(self):
        if self.currentCoffee == None:
            raise ValueError("No Coffee selected")
        print(f"Your {self.currentCoffee.type} is complete.")
        self.give_out_change()
        self.currentCoffee = None
