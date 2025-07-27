from item import Item

class Catalog:
    def __init__(self):
        self.items:dict[str, Item]= {}
    
    def update_item(self, item: Item):
        self.items[item.barcode] = item
    
    def remove_item(self, item: Item):
        self.items.pop(item.barcode)

    def get_item(self, barcode: str):
        self.items.get(barcode)
    
