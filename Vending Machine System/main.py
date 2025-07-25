
# write code here which uses all teh classes defined in this folder and 
# demonstrates the functionality of the vending machine system.

# write code here which uses all teh classes defined in this folder and 
# demonstrates the functionality of the vending machine system.

from VendingMachine import VendingMachine
from Product import Product
from PaymentProcessor import PaymentProcessor
from Rack import Rack
from InventoryManager import InventoryManager
from Transaction import Transaction
def main():
    # Create products
    product1 = Product("Soda","Soda", 150)
    product2 = Product("Chips","Chips", 100)

    # Create racks
    rack1 = Rack("R1", product1, 10)
    rack2 = Rack("R2", product2, 5)

    # Create inventory manager and update racks
    inventory_manager = InventoryManager()
    inventory_manager.update_rack({"R1": rack1, "R2": rack2})

    # Create payment processor with initial balance
    payment_processor = PaymentProcessor()

    # Create a transaction
    current_transaction = Transaction(rack1, product1, 200)

    # Create vending machine
    vending_machine = VendingMachine(inventory_manager, payment_processor, current_transaction)

    # Simulate user actions
    vending_machine.insert_money(200)
    selected_product = vending_machine.chooseProduct("R1")
    
    print(f"Selected Product: {selected_product.product_code}, Price: {selected_product.unit_price}")
    
    vending_machine.confirm_transaction()
    
    print(f"Product dispensed: {selected_product.product_code}")

    print("Transaction History:", vending_machine.get_transaction_history())
    print("Remaining Balance:", payment_processor.current_balance)

    print("Change returned:", vending_machine.return_change())

    print("Remaining Balance:", payment_processor.current_balance)
if __name__ == "__main__":
    main()