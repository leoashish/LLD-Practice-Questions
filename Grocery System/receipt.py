from order import Order
import datetime


class receipt:
    def __init__(self, id: int, order: Order):
        self.receipt_id = id
        self.order = order
        self.issue_date = datetime.datetime

    def print_receipt(self):
        print(
            f"Receipt: {self.receipt_id}, Order: {self.order.order_id}, Date: {self.issue_date}"
        )
