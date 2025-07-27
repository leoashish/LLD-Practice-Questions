from item import Item
from discount_campaign import DiscountCampaign


class OrderItem:
    def __init__(self, item: Item, quantity: int):
        self.item = item
        self.quantity = quantity

    def calculate_price(self) -> float:
        return self.item.price * self.quantity

    def calculate_price_with_discount(self, newDiscount: DiscountCampaign) -> float:
        return newDiscount.calculate_discount(self) * self.quantity
