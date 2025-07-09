package models;
import java.math.BigDecimal;

public interface FareStrategy {
    public BigDecimal calculateFare(Ticket ticket, BigDecimal inputfare);
}
