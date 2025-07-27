from CoffeeMakerSystem import CoffeeMakerSystem
from Ingredient import Ingredient
from BlackCoffeeRecipe import BlackCoffeeRecipe
from Cappicino import CappicinoRecipe
from coffeeModel import CoffeeModel


def main():
    # Create ingredients
    water = Ingredient("Water")
    coffee = Ingredient("Coffee")
    milk = Ingredient("Milk")
    sugar = Ingredient("Sugar")

    # Create a recipe for coffee
    black_coffee_recipe = BlackCoffeeRecipe(ingredients={water: 10, coffee: 10})
    cappuccino_recipe = CappicinoRecipe(ingredients={water: 10, coffee: 5})
    black_coffee = CoffeeModel(type="Black Coffee", cost=5, recipe=black_coffee_recipe)
    cappuccino = CoffeeModel(type="Cappuccino", cost=7, recipe=cappuccino_recipe)
    # Initialize the coffee vending machine and add ingredients
    machine = CoffeeMakerSystem()
    machine.fill_inventory(water, 100)
    machine.fill_inventory(coffee, 50)
    machine.fill_inventory(milk, 30)
    machine.fill_inventory(sugar, 20)

    # Add recipe to the machine
    machine.insert_coffee_types(black_coffee)
    machine.insert_coffee_types(cappuccino)

    # Select recipe and make coffee
    machine.selectCoffee(black_coffee)
    machine.receive_payment(10)

    machine.brew_coffee()
    machine.dispence_coffee()


if __name__ == "__main__":
    main()
