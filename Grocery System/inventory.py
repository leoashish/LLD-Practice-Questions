class Inventory:
    def __init__(self):
        self.stocks: dict[str, int] = {}

    def add_stock(self, barcode:str, count:int):
        if barcode in self.stocks:
            self.stocks[barcode] += count
        else:
            self.stocks[barcode] = count
    
    def reduce_stock(self, barcode: str, count: int):
        self.stocks[barcode] -= count

    def get_stock(self, barcode:str):
        return self.stocks[barcode]