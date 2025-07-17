package UnixFileSearchSystem.src.Models;

public interface ComparisonOperator<T> {
    public boolean isMatch(final T attributeValue, final T expectedValue);
}
