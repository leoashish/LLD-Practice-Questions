from order import Order
from item import Item
from discount_campaign import DiscountCampaign


class Checkout:
    def __init__(self, current_order: Order):
        self.current_order: Order = current_order
        self.discounts: list[DiscountCampaign] = []

    def start_new_order(self):
        self.current_order = Order()

    def add_item_to_order(self, item: Item, quantity: int):
        self.current_order.add_item(item)
