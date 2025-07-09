package models;
public class MoterCycle implements  Vehicle{
    public String LicensePlate;
    public VehicleSize size;
    public MoterCycle(String licensePlate) {
        super();
        this.LicensePlate = licensePlate;
        this.size = VehicleSize.SMALL;
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
