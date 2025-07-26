from abc import ABC, abstractmethod
from ElevatorCar import ElevatorCar
from Direction import Direction
from typing import List
class DispatchingStrategy(ABC):
    @abstractmethod
    def select_elevator(self, elevators: List[ElevatorCar], floor: int, direction: Direction)->ElevatorCar:
        pass
