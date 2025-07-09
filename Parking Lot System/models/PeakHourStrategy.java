package models;

import java.math.BigDecimal;

public class PeakHourStrategy implements FareStrategy {

    public static final BigDecimal PEAK_HOUR_RATE = new BigDecimal("2.0");

    @Override
    public BigDecimal calculateFare(Ticket ticket, BigDecimal inputFare) {
        var fare = inputFare;
        fare = fare.add(PEAK_HOUR_RATE.multiply(new BigDecimal(ticket.getParkingDuration())));
        return fare;
    }
    
}
