from discount_criteria import DiscountCriteria
class ItemBasedCriteria(DiscountCriteria):
    def __init__(self, is_applicable:bool, barcode:str):
        self.is_applicable = is_applicable
        self.barcode = barcode
    
    def get_barcode(self)->str:
        return self.barcode