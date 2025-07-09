package models;
public class Car implements Vehicle {

    public VehicleSize size;
    public String licensePlate;
    public Car(String licensePlate) {
        this.licensePlate = licensePlate;
        this.size = VehicleSize.MEDIUM;
    }
    @Override
    public String getLicensePlate() {
        return this.licensePlate;
    }

    @Override
    public VehicleSize getVehicleSize() {
        return this.size;
    }
    
}
