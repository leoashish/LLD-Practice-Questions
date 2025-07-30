from abc import ABC, abstractmethod


class rate_limiting_strategy(ABC):
    def __init__(self, limit, time_period_min):
        self.limit = limit

    @abstractmethod
    def rate_limit(self, request) -> bool:
        pass
