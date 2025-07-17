package UnixFileSearchSystem.src.Models;


public class FileSearchCriteria {
    private final Predicate predicate;
    
    public FileSearchCriteria(Predicate predicate) {
        this.predicate = predicate;
    }

    public boolean isMatch(File file){
        return this.predicate.isMatch(file);
    }
}
