from discount_campaign import DiscountCampaign
from order_item import OrderItem
from item import Item


class Order:
    def __init__(
        self,
        order_id: int,
        appliedDiscounts: dict[OrderItem, DiscountCampaign],
        payment_amount: float,
    ):
        self.items: list[Item] = []
        self.order_id = order_id
        self.appliedDiscounts = appliedDiscounts
        self.payment_amount = payment_amount

    def add_item(self, item: Item):
        self.items.append(item)

    def calculate_subtotal(self):
        pass

    def calculate_total(self):
        pass

    def calculate_change(self):
        pass

    def apply_discount(self, item, discount: DiscountCampaign):
        pass
