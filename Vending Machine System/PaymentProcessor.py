class PaymentProcessor:
    def __init__(self):
        self.current_balance = 0
    
    def add_balance(self, balance: int):
        self.current_balance += balance

    def charge(self, amount):
        self.current_balance -= amount
    
    def return_change(self)->int:
        change = self.current_balance
        self.current_balance = 0
        return change
    
    def get_balance(self)->int:
        return self.current_balance

