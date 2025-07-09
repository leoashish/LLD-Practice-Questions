package models;

import java.time.Duration;
import java.time.LocalDateTime;
import java.util.UUID;

public class Ticket {
    public final String ticketId;
    public final Vehicle vehicle;
    public final ParkingSpot spot;
    public final LocalDateTime entryTime;
    public LocalDateTime exitTime;

    public Ticket(Vehicle vehicle, ParkingSpot spot, LocalDateTime entryTime) {
        super();
        this.ticketId = UUID.randomUUID().toString();
        this.vehicle = vehicle;
        this.spot = spot;
        this.entryTime = entryTime;
    }

    public int getParkingDuration(){
        var duration= Duration.between(this.entryTime, this.exitTime);
        return (int)duration.toMinutes();
    }
}
