from Recipe import Recipe


class CoffeeModel:
    def __init__(self, type, cost, recipe):
        self.type = type
        self.cost = cost
        self.recipe: Recipe = recipe
