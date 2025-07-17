package UnixFileSearchSystem.src.Models;

public class NotPredicate implements CompositePredicate {
    private Predicate operand;

    public NotPredicate(final Predicate operand) {
        this.operand = operand;
    }
    @Override
    public boolean isMatch(File file) {
        return !operand.isMatch(file);
    }
    
}
