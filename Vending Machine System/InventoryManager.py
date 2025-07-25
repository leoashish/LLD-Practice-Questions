from Rack import Rack
from Product import Product

class InventoryManager:
    def __init__(self):
        self.racks_dict:dict[str, Rack] = {}

    def update_rack(self, updated_racks: dict[str, Rack]):
        for rackCode in updated_racks.keys():
            rack = updated_racks[rackCode]
            self.racks_dict[rackCode] = rack
    
    def get_product_in_rack(self, rack_code: str)->Product:
        if rack_code in self.racks_dict:
            return self.racks_dict[rack_code].product
        else:
            raise KeyError("The given key does not exists.")
        
    def dispense_product_from_rack(self, rack_code: str)->Product:
        if rack_code in self.racks_dict:
            rack = self.racks_dict[rack_code]
            product = rack.product
            rack.count -=1
            return product
        else:
            raise KeyError("The given key does not exists.")
        
