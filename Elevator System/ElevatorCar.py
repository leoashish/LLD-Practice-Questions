from ElevatorStatus import ElevatorStatus
from Direction import Direction
class ElevatorCar:
    def __init__(self, starting_floor):
        self.status = ElevatorStatus(starting_floor, Direction.IDLE)
        self.target_floors = []

    def get_status(self):
        return self.status
    
    def add_floor_request(self, floor:int):
        if floor not in self.target_floors:
            self.target_floors.append(floor)
            self.update_direction(floor)
    
    def is_idle(self)->bool:
        return self.status == Direction.IDLE
    
    def update_direction(self, target_floor:int):
        status = self.status
        current_floor = status.current_floor
        if target_floor > current_floor:
            status.current_direction = Direction.UP
        elif target_floor < current_floor:
            status.current_direction = Direction.DOWN