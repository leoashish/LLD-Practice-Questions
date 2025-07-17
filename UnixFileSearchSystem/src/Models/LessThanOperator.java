package UnixFileSearchSystem.src.Models;


public class LessThanOperator<T extends Number> implements ComparisonOperator<T> {

    @Override
    public boolean isMatch(T attributeValue, T expectedValue) {
        return Double.compare(attributeValue.doubleValue(), expectedValue.doubleValue()) < 0;
    }
    
}
