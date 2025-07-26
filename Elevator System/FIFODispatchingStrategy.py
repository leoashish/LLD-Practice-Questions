from DispatchingStrategy import DispatchingStrategy
from ElevatorCar import ElevatorCar
from Direction import Direction
from typing import List, override
import random
class FIFODispatchingStrategy(DispatchingStrategy):
     
    @override
    def select_elevator(self, elevators:List[ElevatorCar], floor:int, direction: Direction)->ElevatorCar:
        for e in elevators:
            if e.status.current_direction == direction or e.status.current_direction == Direction.IDLE:
                return e
        return elevators[random.randint(0, len(elevators))]
        
                