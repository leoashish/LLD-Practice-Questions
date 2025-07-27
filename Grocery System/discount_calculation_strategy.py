from abc import abstractmethod


class DiscountCalculationStrategy:
    @abstractmethod
    def calculate_discounted_price(self, original_price: float) -> float:
        pass
