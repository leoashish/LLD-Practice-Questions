package models;

public class Bus implements Vehicle{
    public String LicensePlate;
    public VehicleSize size;
    public Bus(String licensePlate) {
        super();
        this.LicensePlate = licensePlate;
        this.size = VehicleSize.LARGE;
    }
    @Override
    public String getLicensePlate() {
        return this.LicensePlate;
    }

    @Override
    public VehicleSize getVehicleSize() {
        return this.size;
    }
    
}
