package models;

import java.time.LocalDateTime;

public class ParkingLot {
    public final ParkingManager parkingManager;
    public FareCalculator fareCalculator;

    public ParkingLot(ParkingManager parkingManager, FareCalculator fareCalculator) {
        super();
        this.parkingManager = parkingManager;
        this.fareCalculator = fareCalculator;
    }

    public Ticket enterVehicle(Vehicle vehicle){
        var spot = parkingManager.parkVehicle(vehicle);
        if(spot != null){
            Ticket ticket = new Ticket(vehicle, spot, LocalDateTime.now());
            System.out.println("Vehicle parked to spot number: " + spot.getSpotNumber());
            return ticket;
        }else{
            System.out.println("No available parking spot for vehicle:" + vehicle.getLicensePlate());
            return null;
        }
    }

    public void leaveVehicle(Ticket ticket){
        if(ticket != null && ticket.exitTime == null){
            ticket.exitTime = LocalDateTime.now();
            parkingManager.unParkVehicle(ticket.vehicle);
            var fare = fareCalculator.calculateFare(ticket);
            System.out.println("Vehicle with license plate " + ticket.vehicle.getLicensePlate() + 
                               " has left the parking lot. Fare: " + fare);
        }else{
            System.out.println("Invalid ticket or vehicle has already left the parking lot.");
        }
    }
}
