package models;
import java.math.BigDecimal;

public class BaseFareStrategy implements FareStrategy{
    
    public static final BigDecimal SMALL_VEHICLE_RATE = new BigDecimal("1.0");

    public static final BigDecimal MID_VEHICLE_RATE = new BigDecimal("1.5");

    public static final BigDecimal LARGE_VEHICLE_RATE = new BigDecimal("2.0");
    @Override
    public BigDecimal calculateFare(Ticket ticket, BigDecimal inputfare) {
        var fare = inputfare;
        BigDecimal rate;
        switch (ticket.vehicle.getVehicleSize()) {
            case SMALL -> rate = SMALL_VEHICLE_RATE;
            case MEDIUM -> rate = MID_VEHICLE_RATE;
            case LARGE -> rate = LARGE_VEHICLE_RATE;
            default -> rate = BigDecimal.ZERO;
        }
      fare.add(rate.multiply(new BigDecimal(ticket.getParkingDuration())));
      return fare;
    }
    
}
