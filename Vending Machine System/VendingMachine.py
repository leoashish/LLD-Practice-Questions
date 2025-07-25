from Rack import Rack
from PaymentProcessor import PaymentProcessor
from Transaction import Transaction
from InventoryManager import InventoryManager
from Product import Product 
class VendingMachine:
    def __init__(self, inventory_manager:InventoryManager, payment_processor:PaymentProcessor, current_transaction: Transaction):
        self.inventory_manager = inventory_manager
        self.payment_processor = payment_processor
        self.current_transaction = current_transaction
        self.all_transactions = []

    def set_racks(self, racks_dictionary: dict[str,Rack]):
        self.inventory_manager.update_rack(racks_dictionary)
    
    def insert_money(self, amount: int):
        self.payment_processor.add_balance(amount)
    
    def chooseProduct(self, rack_code: str)->Product:
        return  self.inventory_manager.get_product_in_rack(rack_code)
    
    def confirm_transaction(self):
        if self.current_transaction is None:
            raise ValueError("No transaction to confirm.")
        self.validate_transaction()
        self.payment_processor.charge(self.current_transaction.product.unit_price)
        self.inventory_manager.dispense_product_from_rack(self.current_transaction.rack.rack_code)
        self.all_transactions.append(self.current_transaction)
        product = self.current_transaction.product

    def validate_transaction(self):
        if self.current_transaction is None:
            raise ValueError("No transaction to validate.")
        rack:Rack = self.current_transaction.rack
        product:Product = self.current_transaction.product
        amount:int = self.current_transaction.amount
        if rack.count <=0:
            raise ValueError("The product is out of stock.")
        if product.unit_price > amount:
            raise ValueError("Insufficient balance to purchase the product.")

    def cancel_transaction(self):
        self.payment_processor.return_change()
        self.all_transactions.append(self.current_transaction)
        self.current_transaction = None
    
    def get_transaction_history(self):
        return self.all_transactions

    def return_change(self):
        return self.payment_processor.return_change()

    