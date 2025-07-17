package UnixFileSearchSystem.src.Models;

import java.util.List;

public class OrPredicate implements CompositePredicate {
    private List<Predicate> operands;

    public OrPredicate(final List<Predicate> operands) {
        this.operands = operands;
    }
    @Override
    public boolean isMatch(File file) {
        return operands.stream()
        .anyMatch(predicate-> 
        predicate.isMatch(file));
    }
    
}