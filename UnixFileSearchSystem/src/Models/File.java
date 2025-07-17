package UnixFileSearchSystem.src.Models;
import java.util.HashSet;
import java.util.Set;

public class File {
    private int size;
    private String owner;
    private String filename;
    private boolean isDirectory;
    
    private final Set<File> entries = new HashSet<>();

    public File(int size, String owner,String filename, boolean isDirectory) {
        this.size = size;
        this.owner = owner;
        this.filename = filename;
        this.isDirectory = isDirectory;
    }


    public Object extract(FileAttribute fileAttribute){
        switch(fileAttribute){
            case SIZE->{
                return size;
            }
            case OWNER ->{
                return owner;
            }
            case FILENAME ->{
                return filename;
            }
            case IS_DIRECTORY->{
                return isDirectory;
            }
        }

        throw new IllegalArgumentException();
    }

    public void addEntry(File file){
        this.entries.add(file);
    }

    public Set<File> getEntries(){
        return entries;
    }
}
