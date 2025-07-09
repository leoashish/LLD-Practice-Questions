package models;

import java.math.BigDecimal;
import java.util.List;

public class FareCalculator {
    private final List<FareStrategy> strategies;

    public FareCalculator(List<FareStrategy> strategies){
        this.strategies = strategies;
    }

    public BigDecimal calculateFare(Ticket ticket){
        BigDecimal fare = BigDecimal.ZERO;
        for (FareStrategy strategy : strategies){
            fare= strategy.calculateFare(ticket, fare);
        }
        return fare;
    }
}
