package models;
public class CompactSpot implements ParkingSpot {
    private final int spotNumber;
    private Vehicle vehicle;

    public CompactSpot(int spotNumber, Vehicle vehicle) {
        super();
        this.spotNumber = spotNumber;
        this.vehicle = vehicle;
    }

    @Override
    public boolean isAvailable() {
        return this.vehicle == null;
    }

    @Override
    public void occupy(Vehicle vehicle) {
        this.vehicle = vehicle;
    }

    @Override
    public void vacate() {
        this.vehicle = null;
    }

    @Override
    public int getSpotNumber() {
        return this.spotNumber;
    }

    @Override
    public VehicleSize getVehicleSize() {
        return this.vehicle.getVehicleSize();
    }
    
}
