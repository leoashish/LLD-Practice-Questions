from discount_criteria import DiscountCriteria
from discount_calculation_strategy import DiscountCalculationStrategy
from item import Item
from order_item import OrderItem


class DiscountCampaign:
    def __init__(
        self,
        discount_id: str,
        name: str,
        criteria: DiscountCriteria,
        calculation_strategy: DiscountCalculationStrategy,
    ):
        self.discount_id = discount_id
        self.name = name
        self.criteria = criteria
        self.calculation_strategy = calculation_strategy

    def is_applicable(self, item: Item) -> float:
        return self.criteria.is_applicable

    def calculate_discount(self, order_item: OrderItem) -> float:
        return self.calculation_strategy.calculate_discounted_price(
            order_item.item.price
        )
