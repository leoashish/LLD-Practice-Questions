package UnixFileSearchSystem.src.Models;

public interface Predicate {
    public boolean isMatch(File file);
}
