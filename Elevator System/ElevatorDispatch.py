from Direction import Direction
from ElevatorCar import ElevatorCar
from typing import List
from DispatchingStrategy import DispatchingStrategy

class ElevatorDispatch:

    def __init__(self, strategy:DispatchingStrategy):
        self.strategy = strategy

    def dispatch_elevator_car(self, floor:int, direction:Direction, elevators: List[ElevatorCar]):
        selected_elevator = self.strategy.select_elevator(elevators, floor, direction)
        if selected_elevator != None:
            selected_elevator.target_floors.append(floor)