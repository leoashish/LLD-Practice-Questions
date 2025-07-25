from Product import Product
class Rack:
    def __init__(self, rack_code:str, product:Product, count: int):
        self.rack_code = rack_code
        self.product = product
        self.count = count

    def get_product(self)->Product:
        return self.product
    
    def get_product_count(self)->int:
        return self.count