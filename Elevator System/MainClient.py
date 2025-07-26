from ElevatorSystem import ElevatorSystem
from FIFODispatchingStrategy import FIFODispatchingStrategy
from DispatchingStrategy import DispatchingStrategy
from ElevatorDispatch import ElevatorDispatch
from Direction import Direction
from ElevatorCar import ElevatorCar
def main():
    # Create elevators
    elevator1 = ElevatorCar(0)
    elevator2 = ElevatorCar(0)

    # Create floors
    floors = [(i) for i in range(6)]  # Floors 0 to 
    elevatorDispatchContorller= ElevatorDispatch(FIFODispatchingStrategy())
    # Create elevator system
    elevator_system = ElevatorSystem(elevators=[elevator1, elevator2], dispatchController=elevatorDispatchContorller)

    # Simulate requests
    print("Initial Elevator States:")
    for elevator in elevator_system.elevators:
        print(elevator)

    # User at floor 0 requests to go up to floor 4
    elevator_system.request_elevator(current_floor=0, direction=Direction.UP)

    elevator_system.select_floor(elevator1, 4)  # Select floor 4 for elevator 1
    
    # Print final states
    print("Final Elevator States:")
    for elevator in elevator_system.elevators:
        print(elevator)

if __name__ == "__main__":
    main()