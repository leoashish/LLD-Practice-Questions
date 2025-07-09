package models;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ParkingManager {
    private final Map<Vehicle, ParkingSpot> vehicleToParkingSpotMap;
    private final Map<VehicleSize, List<ParkingSpot>> availableSpots;

    public ParkingManager(Map<VehicleSize, List<ParkingSpot>> availableSpots) {
        super();
        this.availableSpots = availableSpots;
        this.vehicleToParkingSpotMap = new HashMap<>();
    }
    
    public ParkingSpot findParkingSpotForVehicle(Vehicle vehicle){
        
        for(VehicleSize size: VehicleSize.values()){
            if(size.ordinal() >= vehicle.getVehicleSize().ordinal()){
                if(availableSpots.get(size).isEmpty()){
                    var spots = availableSpots.get(size);
                    for(var spot: spots){
                        if(spot.isAvailable()){
                            return spot;
                        }
                    }
                }
            }
        }
        return null;
    }

    public ParkingSpot parkVehicle(Vehicle vehicle){
        var spot = findParkingSpotForVehicle(vehicle);
        if(spot != null){
            spot.occupy(vehicle);
            this.vehicleToParkingSpotMap.put(vehicle, spot);
            this.availableSpots.get(vehicle.getVehicleSize()).remove(spot);
        }
        return null;
    }
    public void unParkVehicle(Vehicle vehicle){
        var spot = this.vehicleToParkingSpotMap.get(vehicle);
        if(spot != null){
            spot.vacate();
            this.availableSpots.get(spot.getVehicleSize()).add(spot);
        }
    }
}
