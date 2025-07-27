from abc import ABC


class DiscountCriteria(ABC):
    def __init__(self) -> None:
        self.is_applicable: bool
