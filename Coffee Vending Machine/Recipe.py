from abc import ABC, abstractmethod


class Recipe(ABC):
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @abstractmethod
    def make_coffee(self):
        pass
