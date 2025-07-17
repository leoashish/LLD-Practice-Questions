package UnixFileSearchSystem.src.Models;

public class SimplePredicate<T>  implements Predicate{
    private FileAttribute attribute;
    private ComparisonOperator<T> operator;
    T expectedValue;

    public SimplePredicate(
    final FileAttribute fileAttribute,
    final ComparisonOperator<T> comparisonOperator,
    final T expectedValue ) {   
    
        this.attribute = fileAttribute;
        this.operator = comparisonOperator;
        this.expectedValue = expectedValue;
    
    }
    @Override
    public boolean isMatch(final File inputFile) {
        Object actualValue = inputFile.extract(attribute);
        if(expectedValue.getClass().isInstance(actualValue)){
            return this.operator.isMatch((T)actualValue, expectedValue);
        }
        return false;
    }
    
}
