from typing import List
from ElevatorStatus import ElevatorStatus
from ElevatorCar import ElevatorCar
from Direction import Direction
from ElevatorDispatch import ElevatorDispatch
class ElevatorSystem:
    def __init__(self, elevators, dispatchController):
        self.elevators:List[ElevatorCar]= elevators
        self.dispatchController:ElevatorDispatch = dispatchController
    
    def get_elevator_statuses(self)->List[ElevatorStatus]:
        return [s.status for s in self.elevators]
    
    def request_elevator(self, current_floor: int, direction: Direction):
        self.dispatchController.dispatch_elevator_car(current_floor, direction, self.elevators)
    
    def select_floor(self, elevator_car: ElevatorCar, destination_floor: int):
        elevator_car.add_floor_request(destination_floor)
