from discount_criteria import DiscountCriteria
class CategoryBasedCriteria(DiscountCriteria):
    def __init__(self, is_applicable:bool, category:str):
        self.is_applicable = is_applicable
        self.category = category
    
    def get_category(self)->str:
        return self.category