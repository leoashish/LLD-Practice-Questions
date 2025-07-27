from discount_calculation_strategy import DiscountCalculationStrategy
from typing import override


class PercentBasedStrategy(DiscountCalculationStrategy):
    def __init__(self, discountPercentage: float):
        self.discount_percentage = discountPercentage

    @override
    def calculate_discounted_price(self, original_price: float) -> float:
        return original_price * (1 - self.discount_percentage / 100)
