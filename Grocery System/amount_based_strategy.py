from typing import override
from discount_calculation_strategy import DiscountCalculationStrategy


class AmountBasedStrategy(DiscountCalculationStrategy):
    def __init__(self, discounted_amount: int):
        self.discounted_amount = discounted_amount

    @override
    def calculate_discounted_price(self, original_price: float) -> float:
        return original_price - self.discounted_amount
